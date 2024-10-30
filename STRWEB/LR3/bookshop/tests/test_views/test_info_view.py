from django.test import TestCase
from django.urls import reverse
from app.app_models.commonModels import AboutInfo


class AboutInfoViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        AboutInfo.objects.create(info='Test Info')

    def test_get(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertEquals(response.context[0]['info']['info'], 'Test Info')

    def test_get_by_name(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertEquals(response.context[0]['info']['info'], 'Test Info')

    def test_post_invalid(self):
        session = self.client.session
        session['role'] = 'emp'
        session.save()
        response = self.client.post(reverse('about'), {'action': 'upd'})
        self.assertEquals(response.status_code, 302)

    def test_post_upd(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('about'), {'action': 'upd'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertIsNotNone(response.context[0]['form'])

    def test_post_save_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(
            reverse('about'), {'action': 'save', 'info': 'Upd info'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(AboutInfo.objects.first().info, 'Upd info')

    def test_post_save_invalid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(
            reverse('about'), {'action': 'save', 'info': ''})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['form'].errors['info'], [
                          'This field is required.'])
