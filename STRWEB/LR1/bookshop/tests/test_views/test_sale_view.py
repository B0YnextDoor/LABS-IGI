from django.test import TestCase
from django.urls import reverse
from app.app_models.commonModels import SaleCode


class SaleViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        SaleCode.objects.create(code='code_10', is_active=True)
        SaleCode.objects.create(code='code_20', is_active=False)

    def test_get_invalid(self):
        response = self.client.get('/sales/')
        self.assertEquals(response.status_code, 302)

    def test_get_customer(self):
        session = self.client.session
        session['role'] = 'usr'
        session.save()
        response = self.client.get('/sales/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'salecodes.html')
        codes = response.context[0]['codes']
        self.assertIsNotNone(codes)
        self.assertEquals(len(codes), 1)

    def test_get_admin(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.get('/sales/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'salecodes.html')
        codes = response.context[0]['codes']
        self.assertIsNotNone(codes)
        self.assertEquals(len(codes), 2)

    def test_get_by_name(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.get(reverse('sale'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'salecodes.html')
        codes = response.context[0]['codes']
        self.assertIsNotNone(codes)
        self.assertEquals(len(codes), 2)

    def test_post_invalid(self):
        response = self.client.post(reverse('sale'))
        self.assertEquals(response.status_code, 302)

    def test_post_add(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('sale'), {'action': 'add'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'salecodes.html')
        self.assertIsNotNone(response.context[0]['form'])

    def test_post_del(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('sale'), {'action': 'del_1'})
        self.assertEquals(response.status_code, 302)
        codes = SaleCode.objects.all()
        self.assertIsNotNone(codes)
        self.assertEquals(len(codes), 1)
        self.assertEquals(codes[0].id, 2)

    def test_post_upd(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('sale'), {'action': 'upd_1'})
        self.assertEquals(response.status_code, 302)
        codes = SaleCode.objects.all()
        self.assertIsNotNone(codes)
        self.assertEquals(len(codes), 2)
        self.assertFalse(codes[0].is_active)

    def test_post_save_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(
            reverse('sale'), {'action': 'save', 'code': 'code_50', 'is_active': False})
        self.assertEquals(response.status_code, 302)
        codes = SaleCode.objects.all()
        self.assertIsNotNone(codes)
        self.assertEquals(len(codes), 3)
        self.assertEquals(codes[1].code, 'code_50')
        self.assertFalse(codes[1].is_active)

    def test_post_save_invalid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(
            reverse('sale'), {'action': 'save', 'code': 'code50', 'is_active': False})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'salecodes.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['form'].non_field_errors()[
                          0], 'Sale code must match `code-part`_`sale-part`')
