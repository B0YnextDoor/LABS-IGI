from django.test import TestCase
from django.urls import reverse
from app.app_models.commonModels import QA


class QAViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        QA.objects.create(question='Test Question1', answer='Test Answer1')
        QA.objects.create(question='Test Question2', answer='Test Answer2')

    def test_get(self):
        session = self.client.session
        session['role'] = ''
        session.save()
        response = self.client.get('/faq/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'qa.html')
        qas = response.context[0]['qas']
        self.assertEquals(len(qas), 2)
        self.assertEquals(qas[0].question, 'Test Question1')

    def test_get_by_name(self):
        session = self.client.session
        session['role'] = ''
        session.save()
        response = self.client.get(reverse('faq'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'qa.html')
        qas = response.context[0]['qas']
        self.assertEquals(len(qas), 2)
        self.assertEquals(qas[0].question, 'Test Question1')

    def test_post_invalid(self):
        session = self.client.session
        session['role'] = 'usr'
        session.save()
        response = self.client.post(reverse('faq'))
        self.assertEquals(response.status_code, 302)

    def test_post_add(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('faq'), {'action': 'add'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'qa.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['action'], 'add')

    def test_post_del(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('faq'), {'action': 'del_1'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(QA.objects.count(), 1)
        self.assertEquals(QA.objects.first().question, 'Test Question2')

    def test_post_upd_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('faq'), {'action': 'upd_1'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'qa.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['action'], 1)

    def test_post_upd_invalid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('faq'), {'action': 'upd_3'})
        self.assertEquals(response.status_code, 302)

    def test_post_save_add_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(
            reverse('faq'), {'action': 'save_add', 'question': 'WUT?', 'answer': 'YEP'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(QA.objects.count(), 3)
        self.assertIsNotNone(QA.objects.get(id=3))
        self.assertEquals(QA.objects.get(id=3).question, 'WUT?')

    def test_post_save_add_invalid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(
            reverse('faq'), {'action': 'save_add', 'question': 'WUT?', 'answer': ''})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'qa.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['form'].errors['answer'], [
                          'This field is required.'])
        self.assertEquals(response.context[0]['action'], 'add')

    def test_post_save_upd_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(
            reverse('faq'), {'action': 'save_1', 'question': 'WUT?', 'answer': 'YEP'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(QA.objects.count(), 2)
        self.assertIsNotNone(QA.objects.get(id=1))
        self.assertEquals(QA.objects.get(id=1).question, 'WUT?')

    def test_post_save_upd_invalid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(
            reverse('faq'), {'action': 'save_1', 'question': 'WUT?', 'answer': ''})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'qa.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['form'].errors['answer'], [
                          'This field is required.'])
        self.assertEquals(response.context[0]['action'], '1')
