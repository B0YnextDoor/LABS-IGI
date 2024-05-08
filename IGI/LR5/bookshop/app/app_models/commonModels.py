from django.urls import reverse
from app.app_models.baseModel import models, BaseModel


class AboutInfo(BaseModel):
    info = models.TextField(default='Default info text',
                            help_text='Company\'s info')

    class Meta:
        db_table = 'about_info_table'

    def __str__(self) -> str:
        return f'{self.id} {self.info} {self.created_at} {self.updated_at}'


class News(BaseModel):
    title = models.CharField(max_length=50, help_text='News title')
    text = models.TextField(help_text='News summary')
    img = models.ImageField(help_text='News photo', blank=True,
                            upload_to='app/static/news', null=True)

    class Meta:
        db_table = 'news_table'
        ordering = ['title']

    def get_absolute_url(self):
        """
        Returns the url to access a particular news instance.
        """
        return reverse('news-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return f'{self.id} {self.title} {self.text} {self.img.url if self.img else "no image"} {self.created_at} {self.updated_at}'


class QA(BaseModel):
    question = models.TextField(help_text='Question')
    answer = models.TextField(help_text='Answer')

    class Meta:
        db_table = 'qa_table'
        ordering = ['id']

    def __str__(self) -> str:
        return f'{self.id} {self.question} {self.answer} {self.created_at} {self.updated_at}'


class Vacancy(BaseModel):
    name = models.CharField(max_length=50, help_text='Vacancy\'s name')
    description = models.TextField(help_text='Vacancy\'s description')

    class Meta:
        db_table = 'vacancies_table'
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.description} {self.created_at} {self.updated_at}'


class SaleCode(BaseModel):
    code = models.CharField(max_length=50, help_text='Sale code')
    is_active = models.BooleanField(help_text='Is code active')

    class Meta:
        db_table = 'sale_codes_table'
        ordering = ['is_active', 'code']

    def __str__(self) -> str:
        return f'{self.id} {self.code} {self.is_active} {self.created_at} {self.updated_at}'
