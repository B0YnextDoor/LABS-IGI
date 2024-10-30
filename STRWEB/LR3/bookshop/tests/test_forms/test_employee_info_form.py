from django.test import TestCase
from app.views.contactView import InfoCreateForm, InfoUpdateForm
from django.core.files.uploadedfile import SimpleUploadedFile
from app.app_models.employeeModels import Employee, EmployeeInfo


class InfoCreateFormTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        e = Employee.objects.create(
            name='Test Employee', phone='+375291111111', email='test@employee.com', password='testpassword', is_admin=False)
        cls.form_data = {
            'employee': (e.id, f'{e.name}, {e.phone}, {e.email}'),
            'image': SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpeg"),
            'description': 'text'
        }

    def test_form_labels(self):
        form = InfoCreateForm()
        self.assertEquals(form.fields['employee'].label, None)
        self.assertEquals(form.fields['image'].label, None)
        self.assertEquals(form.fields['description'].label, None)

    def test_form_help_text(self):
        form = InfoCreateForm()
        self.assertEquals(form.fields['employee'].help_text, '')
        self.assertEquals(form.fields['image'].help_text, 'Employees photo')
        self.assertEquals(
            form.fields['description'].help_text, 'Work description')

    def test_form_invalid(self):
        self.form_data['description'] = ''
        form = InfoCreateForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['description'],
                          ['Description is required!'])


class InfoUpdateFormTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        e = Employee.objects.create(
            name='Test Employee', phone='+375291111111', email='test@employee.com', password='testpassword', is_admin=False)
        EmployeeInfo.objects.create(
            employee_id=e, description='This is a test description', img='/img.png')
        cls.form_data = {
            'image': SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpeg"),
            'description': 'text'
        }

    def test_form_labels(self):
        form = InfoUpdateForm()
        self.assertEquals(form.fields['image'].label, None)
        self.assertEquals(form.fields['description'].label, None)

    def test_form_help_text(self):
        form = InfoUpdateForm()
        self.assertEquals(form.fields['image'].help_text, 'Employees photo')
        self.assertEquals(
            form.fields['description'].help_text, 'Work description')

    def test_form_invalid(self):
        self.form_data['image'] = ''
        form = InfoUpdateForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['image'],
                          ['This field is required.'])
