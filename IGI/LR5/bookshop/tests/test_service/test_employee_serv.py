from django.test import TestCase
from app.app_models import employeeModels as em
from app.services.emloyeeService import EmployeeService


class EmployeeServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        employee = em.Employee.objects.create(
            name='Test Employee', phone='+375291111111', email='test@employee.com', password='testpassword', is_admin=True)
        em.Employee.objects.create(name='Manager', phone='+375292222222',
                                   email='test1@employee.com', password='testpassword', is_admin=False)
        em.EmployeeInfo.objects.create(
            employee_id=employee, description='This is a test description', img='/img.png')

    def test_get_all(self):
        empls = EmployeeService.get_all()
        self.assertIsNotNone(empls)
        self.assertEquals(len(empls), 2)
        self.assertEquals(empls[0].name, 'Test Employee')
        self.assertEquals(empls[0].phone, '+375291111111')
        self.assertEquals(empls[0].email, 'test@employee.com')
        self.assertEquals(empls[0].password, 'testpassword')

    def test_get_by_id(self):
        empl = EmployeeService.get_by_id(1)
        self.assertIsNotNone(empl)
        self.assertEquals(empl.name, 'Test Employee')
        self.assertEquals(empl.phone, '+375291111111')
        self.assertEquals(empl.email, 'test@employee.com')
        self.assertEquals(empl.password, 'testpassword')

    def test_get_by_email(self):
        empl = EmployeeService.get_by_email('test@employee.com')
        self.assertIsNotNone(empl)
        self.assertEquals(empl.name, 'Test Employee')
        self.assertEquals(empl.phone, '+375291111111')
        self.assertEquals(empl.email, 'test@employee.com')
        self.assertEquals(empl.password, 'testpassword')

    def test_update(self):
        empl = EmployeeService.update(
            'test@employee.com', 'Man', '+375291234567', 'test@employee.com', 'test123Test')
        self.assertIsNotNone(empl)
        self.assertEquals(empl.id, 1)
        self.assertEquals(empl.name, 'Man')
        self.assertEquals(empl.phone, '+375291234567')
        self.assertEquals(empl.email, 'test@employee.com')
        self.assertEquals(empl.password, 'test123Test')

    def test_get_info(self):
        has_info, no_info = EmployeeService.get_info()
        self.assertIsNotNone(no_info)
        self.assertEquals(has_info, [])
        self.assertEquals(len(no_info), 1)
        self.assertEquals(no_info[0].id, 2)
        self.assertEquals(no_info[0].name, 'Manager')
        self.assertEquals(no_info[0].phone, '+375292222222')
        self.assertEquals(no_info[0].email, 'test1@employee.com')
        self.assertEquals(no_info[0].password, 'testpassword')

    def test_add_info(self):
        info = EmployeeService.add_info(2, '/img1.png', 'aboba')
        self.assertIsNotNone(info)
        self.assertEquals(info.employee_id.id, 2)
        self.assertEquals(info.employee_id.name, 'Manager')
        self.assertEquals(info.img, '/img1.png')
        self.assertEquals(info.description, 'aboba')

    def test_update_info(self):
        user = EmployeeService.update_info(1, 'imgw.png', 'Text')
        self.assertIsNotNone(user)
        self.assertEquals(user.id, 1)
        self.assertEquals(user.employeeinfo.img, 'imgw.png')
        self.assertEquals(user.employeeinfo.description, 'Text')
