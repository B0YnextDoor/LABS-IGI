from django.test import TestCase
from django.urls import reverse
from app.app_models.employeeModels import Employee, EmployeeInfo


class ContactViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Employee.objects.create(
            name='Test Employee1', phone='+375291111111', email='test1@employee.com', password='testpassword', is_admin=False)
        employee = Employee.objects.create(
            name='Test Employee2', phone='+375292222222', email='test2@employee.com', password='testpassword', is_admin=False)
        EmployeeInfo.objects.create(
            employee_id=employee, description='This is a test description', img='/img.png')

    def test_get(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.get('/contacts/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('contacts.html')
        self.assertEquals(len(response.context[0]['employees']), 1)
        self.assertEquals(
            response.context[0]['employees'][0].name, 'Test Employee2')
        self.assertEquals(len(response.context[0]['no_info']), 1)
        self.assertEquals(
            response.context[0]['no_info'][0].name, 'Test Employee1')

    def test_post_invalid(self):
        response = self.client.post('/contacts/')
        self.assertEquals(response.status_code, 302)

    def test_post_add(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post('/contacts/', {'action': 'add'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('contacts.html')
        self.assertIsNotNone(response.context[0]['form'])

    def test_post_upd(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(
            '/contacts/', {'action': 'upd_2'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('contacts.html')
        self.assertIsNotNone(response.context[0]['form'])

    def test_post_save_invalid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(
            '/contacts/', {'action': 'save_add', 'employee': 1, 'image': '', 'description': 'text'})
        self.assertEquals(response.status_code, 200)
        self.assertIsNotNone(response.context[0]['form'])
