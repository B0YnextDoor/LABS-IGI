from app.app_models.baseModel import models, BaseModel


class Employee(BaseModel):
    name = models.CharField(max_length=50, help_text='Name')
    phone = models.CharField(max_length=13, unique=True,
                             help_text='Phone number')
    email = models.EmailField(
        unique=True, help_text='Email')
    password = models.CharField(max_length=300, help_text='Password')
    is_admin = models.BooleanField(help_text='Admin\Employee')

    class Meta:
        db_table = 'employees_table'
        ordering = ['-is_admin', 'name']

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.phone} {self.email} {self.password} {self.is_admin} \
{self.created_at} {self.updated_at}'


class EmployeeInfo(BaseModel):
    employee_id = models.OneToOneField(
        Employee, on_delete=models.CASCADE)
    img = models.ImageField(help_text='Employees photo',
                            upload_to='app/static/info', null=True, blank=True)
    description = models.TextField(help_text='Employees work description')

    class Meta:
        db_table = 'employees_info_table'
        ordering = ['employee_id']

    def __str__(self) -> str:
        return f'{self.id} {self.employee_id} {self.description} {self.img.url if self.img else "no image"} {self.created_at} {self.updated_at}'
