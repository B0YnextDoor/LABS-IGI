from django.test import TestCase
from django.urls import reverse
from app.app_models.commonModels import Vacancy


class VacancyViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Vacancy.objects.create(
            name='Test Vacancy1', description='This is a test vacancy')
        Vacancy.objects.create(
            name='Test Vacancy2', description='This is a test vacancy')

    def test_get(self):
        response = self.client.get('/vacancies/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacancy.html')
        vacancies = response.context[0]['vacancies']
        self.assertIsNotNone(vacancies)
        self.assertEquals(len(vacancies), 2)

    def test_get_by_name(self):
        response = self.client.get(reverse('vacancies'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacancy.html')
        vacancies = response.context[0]['vacancies']
        self.assertIsNotNone(vacancies)
        self.assertEquals(len(vacancies), 2)

    def test_post_invalid(self):
        response = self.client.post(reverse('vacancies'))
        self.assertEquals(response.status_code, 302)

    def test_post_add(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('vacancies'), {'action': 'add'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacancy.html')
        self.assertIsNotNone(response.context[0]['form'])

    def test_post_upd_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('vacancies'), {'action': 'upd_1'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacancy.html')
        self.assertIsNotNone(response.context[0]['form'])

    def test_post_upd_invalid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('vacancies'), {'action': 'upd_3'})
        self.assertEquals(response.status_code, 302)

    def test_post_del(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('vacancies'), {'action': 'del_1'})
        self.assertEquals(response.status_code, 302)
        vacancies = Vacancy.objects.all()
        self.assertEquals(len(vacancies), 1)
        self.assertIsNone(Vacancy.objects.filter(id=1).first())

    def test_post_save_add_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('vacancies'), {
                                    'action': 'save_add', 'name': 'Test Vacancy3', 'description': 'This is a test vacancy'})
        self.assertEquals(response.status_code, 302)
        vacancies = Vacancy.objects.all()
        self.assertEquals(len(vacancies), 3)
        self.assertIsNotNone(Vacancy.objects.filter(id=3).first())
        self.assertEquals(Vacancy.objects.get(id=3).name, 'Test Vacancy3')

    def test_post_save_add_invalid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('vacancies'), {
                                    'action': 'save_add', 'name': 'Test Vacancy3', 'description': ''})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacancy.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['form'].errors['description'], [
                          'This field is required.'])

    def test_post_save_upd_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('vacancies'), {
                                    'action': 'save_1', 'name': 'Upd vac', 'description': 'This is a test vacancy'})
        self.assertEquals(response.status_code, 302)
        vacancies = Vacancy.objects.all()
        self.assertEquals(len(vacancies), 2)
        self.assertIsNotNone(Vacancy.objects.filter(id=1).first())
        self.assertEquals(Vacancy.objects.get(id=1).name, 'Upd vac')

    def test_post_save_upd_invalid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('vacancies'), {
                                    'action': 'save_1', 'name': 'Test Vacancy3', 'description': ''})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacancy.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['form'].errors['description'], [
                          'This field is required.'])
