from app.app_models.baseModel import models, BaseModel


class Customer(BaseModel):
    name = models.CharField(max_length=50, help_text='Name')
    phone = models.CharField(max_length=13, unique=True,
                             help_text='Phone number')
    email = models.EmailField(
        unique=True, help_text='Email')
    password = models.CharField(
        max_length=300, help_text='Password')

    class Meta:
        db_table = 'customers_table'
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.phone} {self.email} {self.password} {self.created_at} {self.updated_at}'


class CustomerReview(BaseModel):
    user = models.ForeignKey(
        Customer, on_delete=models.CASCADE, help_text='Reviewer')
    rate = models.PositiveSmallIntegerField(help_text='Rate (0-5)')
    text = models.TextField(help_text='Review\'s text')

    class Meta:
        db_table = 'customer_reviews_table'
        ordering = ['rate']

    def __str__(self) -> str:
        return f'{self.id} {self.user.name} {self.rate} {self.text} {self.created_at} {self.updated_at}'
