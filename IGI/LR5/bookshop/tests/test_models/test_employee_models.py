from django.test import TestCase
from app.app_models import employeeModels as em


class EmployeeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        em.Employee.objects.create(name='Test Employee', phone='+375291111111',
                                   email='test@employee.com', password='testpassword', is_admin=True)

    def test_name_label(self):
        employee = em.Employee.objects.get(id=1)
        field_label = employee._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_phone_label(self):
        employee = em.Employee.objects.get(id=1)
        field_label = employee._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')

    def test_email_label(self):
        employee = em.Employee.objects.get(id=1)
        field_label = employee._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_password_label(self):
        employee = em.Employee.objects.get(id=1)
        field_label = employee._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_is_admin_label(self):
        employee = em.Employee.objects.get(id=1)
        field_label = employee._meta.get_field('is_admin').verbose_name
        self.assertEquals(field_label, 'is admin')

    def test_name_max_length(self):
        employee = em.Employee.objects.get(id=1)
        max_length = employee._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_phone_max_length(self):
        employee = em.Employee.objects.get(id=1)
        max_length = employee._meta.get_field('phone').max_length
        self.assertEquals(max_length, 13)

    def test_password_max_length(self):
        employee = em.Employee.objects.get(id=1)
        max_length = employee._meta.get_field('password').max_length
        self.assertEquals(max_length, 300)

    def test_object_name_is_name_phone_email_password_is_admin(self):
        employee = em.Employee.objects.get(id=1)
        expected_object_name = f'{employee.id} {employee.name} {employee.phone} {employee.email} {employee.password} {employee.is_admin} {employee.created_at} {employee.updated_at}'
        self.assertEquals(expected_object_name, str(employee))


class EmployeeInfoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        employee = em.Employee.objects.create(
            name='Test Employee', phone='+375291111111', email='test@employee.com', password='testpassword', is_admin=True)
        em.EmployeeInfo.objects.create(
            employee_id=employee, description='This is a test description', img='/img.png')

    def test_employee_id_label(self):
        employee_info = em.EmployeeInfo.objects.get(id=1)
        field_label = employee_info._meta.get_field('employee_id').verbose_name
        self.assertEquals(field_label, 'employee id')

    def test_img_label(self):
        employee_info = em.EmployeeInfo.objects.get(id=1)
        field_label = employee_info._meta.get_field('img').verbose_name
        self.assertEquals(field_label, 'img')

    def test_description_label(self):
        employee_info = em.EmployeeInfo.objects.get(id=1)
        field_label = employee_info._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_object_name_is_employee_id_description_img(self):
        employee_info = em.EmployeeInfo.objects.get(id=1)
        expected_object_name = f'{employee_info.id} {employee_info.employee_id} {employee_info.description} {employee_info.img.url} {employee_info.created_at} {employee_info.updated_at}'
        self.assertEquals(expected_object_name, str(employee_info))
