from django.test import TestCase
from app.app_models import commonModels as cm


class AboutInfoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cm.AboutInfo.objects.create(info='Test Info')

    def test_info_label(self):
        about_info = cm.AboutInfo.objects.get(id=1)
        field_label = about_info._meta.get_field('info').verbose_name
        self.assertEquals(field_label, 'info')

    def test_object_name_is_info(self):
        about_info = cm.AboutInfo.objects.get(id=1)
        expected_object_name = f'{about_info.id} {about_info.info} {about_info.created_at} {about_info.updated_at}'
        self.assertEquals(expected_object_name, str(about_info))


class NewsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cm.News.objects.create(title='Test News', text='This is a test news.')

    def test_title_label(self):
        news = cm.News.objects.get(id=1)
        field_label = news._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_text_label(self):
        news = cm.News.objects.get(id=1)
        field_label = news._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')

    def test_img_label(self):
        news = cm.News.objects.get(id=1)
        field_label = news._meta.get_field('img').verbose_name
        self.assertEquals(field_label, 'img')

    def test_title_max_length(self):
        news = cm.News.objects.get(id=1)
        max_length = news._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)

    def test_get_absolute_url(self):
        news = cm.News.objects.get(id=1)
        abs_url = news.get_absolute_url()
        self.assertEquals(abs_url, '/news/1')

    def test_object_name_is_title_text_img(self):
        news = cm.News.objects.get(id=1)
        expected_object_name = f'{news.id} {news.title} {news.text} {news.img.url if news.img else "no image"} {news.created_at} {news.updated_at}'
        self.assertEquals(expected_object_name, str(news))


class QAModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cm.QA.objects.create(question='Test Question', answer='Test Answer')

    def test_question_label(self):
        qa = cm.QA.objects.get(id=1)
        field_label = qa._meta.get_field('question').verbose_name
        self.assertEquals(field_label, 'question')

    def test_answer_label(self):
        qa = cm.QA.objects.get(id=1)
        field_label = qa._meta.get_field('answer').verbose_name
        self.assertEquals(field_label, 'answer')

    def test_object_name_is_question_answer(self):
        qa = cm.QA.objects.get(id=1)
        expected_object_name = f'{qa.id} {qa.question} {qa.answer} {qa.created_at} {qa.updated_at}'
        self.assertEquals(expected_object_name, str(qa))


class VacancyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cm.Vacancy.objects.create(
            name='Test Vacancy', description='This is a test vacancy')

    def test_name_label(self):
        vacancy = cm.Vacancy.objects.get(id=1)
        field_label = vacancy._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_description_label(self):
        vacancy = cm.Vacancy.objects.get(id=1)
        field_label = vacancy._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_name_max_length(self):
        vacancy = cm.Vacancy.objects.get(id=1)
        max_length = vacancy._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_name_description(self):
        vacancy = cm.Vacancy.objects.get(id=1)
        expected_object_name = f'{vacancy.id} {vacancy.name} {vacancy.description} {vacancy.created_at} {vacancy.updated_at}'
        self.assertEquals(expected_object_name, str(vacancy))


class SaleCodeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cm.SaleCode.objects.create(code='TestCode', is_active=True)

    def test_code_label(self):
        sale_code = cm.SaleCode.objects.get(id=1)
        field_label = sale_code._meta.get_field('code').verbose_name
        self.assertEquals(field_label, 'code')

    def test_is_active_label(self):
        sale_code = cm.SaleCode.objects.get(id=1)
        field_label = sale_code._meta.get_field('is_active').verbose_name
        self.assertEquals(field_label, 'is active')

    def test_code_max_length(self):
        sale_code = cm.SaleCode.objects.get(id=1)
        max_length = sale_code._meta.get_field('code').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_code_is_active(self):
        sale_code = cm.SaleCode.objects.get(id=1)
        expected_object_name = f'{sale_code.id} {sale_code.code} {sale_code.is_active} {sale_code.created_at} \
{sale_code.updated_at}'
        self.assertEquals(expected_object_name, str(sale_code))
