from django.test import TestCase
from app.app_models import commonModels as cm
from app.services.commonService import *


class InfoServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cm.AboutInfo.objects.create(info='Test Info')

    def test_get(self):
        info = InfoService.get()
        self.assertIsNotNone(info)
        self.assertEquals(info['info'], 'Test Info')

    def test_update(self):
        updated_info = InfoRepository.update('Updated Info')
        self.assertIsNotNone(updated_info)
        self.assertEquals(updated_info.info, 'Updated Info')


class NewsServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cm.News.objects.create(title='Test News', text='This is a test news.')

    def test_get_all(self):
        news = NewsService.get_all()
        self.assertIsNotNone(news)
        self.assertEquals(len(news), 1)
        self.assertEquals(news[0]['title'], 'Test News')

    def test_get_by_id(self):
        news = NewsService.get_by_id(1)
        self.assertIsNotNone(news)
        self.assertEquals(news.id, 1)
        self.assertEquals(news.title, 'Test News')
        self.assertEquals(news.text, 'This is a test news.')

    def test_create(self):
        news = NewsService.create('New news', 'Test text', None)
        self.assertIsNotNone(news)
        self.assertEquals(news.title, 'New news')
        self.assertEquals(news.text, 'Test text.')
        self.assertEquals(news.img, None)

    def test_update(self):
        db_news = cm.News.objects.get(id=1)
        news = NewsService.update(1, 'Updated', db_news.text, '/img.png')
        self.assertIsNotNone(news)
        self.assertEquals(news.id, 1)
        self.assertEquals(news.title, 'Updated')
        self.assertEquals(news.text, db_news.text)
        self.assertEquals(news.img, '/img.png')

    def test_delete(self):
        db_news = NewsService.delete(1)
        self.assertEquals(db_news, 'ok')


class QAServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cm.QA.objects.create(question='Test Question', answer='Test Answer')

    def test_get_all(self):
        qas = QAService.get_all()
        self.assertIsNotNone(qas)
        self.assertEquals(len(qas), 1)
        self.assertEquals(qas[0].question, 'Test Question')
        self.assertEquals(qas[0].answer, 'Test Answer')

    def test_get_by_id(self):
        qa = QAService.get_by_id(1)
        self.assertIsNotNone(qa)
        self.assertEquals(qa.question, 'Test Question')
        self.assertEquals(qa.answer, 'Test Answer')

    def test_create(self):
        qa = QAService.create('WUT?', 'YES')
        self.assertIsNotNone(qa)
        self.assertEquals(qa.question, 'WUT?')
        self.assertEquals(qa.answer, 'YES')

    def test_update(self):
        qa = QAService.update(1, 'WUT??', 'NO')
        self.assertIsNotNone(qa)
        self.assertEquals(qa.id, 1)
        self.assertEquals(qa.question, 'WUT??')
        self.assertEquals(qa.answer, 'NO')

    def test_delete(self):
        qa = QAService.delete(1)
        self.assertEquals(qa, 'ok')


class VacancyServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cm.Vacancy.objects.create(
            name='Test Vacancy', description='This is a test vacancy')

    def test_get_all(self):
        vacs = VacancyService.get_all()
        self.assertIsNotNone(vacs)
        self.assertEquals(len(vacs), 1)
        self.assertEquals(vacs[0].name, 'Test Vacancy')
        self.assertEquals(vacs[0].description, 'This is a test vacancy')

    def test_get_by_id(self):
        vac = VacancyService.get_by_id(1)
        self.assertIsNotNone(vac)
        self.assertEquals(vac.name, 'Test Vacancy')
        self.assertEquals(vac.description, 'This is a test vacancy')

    def test_create(self):
        vac = VacancyService.create('New Vac', 'Text')
        self.assertIsNotNone(vac)
        self.assertEquals(vac.name, 'New Vac')
        self.assertEquals(vac.description, 'Text')

    def test_update(self):
        vac = VacancyService.update(1, 'Upd', 'text text')
        self.assertIsNotNone(vac)
        self.assertEquals(vac.id, 1)
        self.assertEquals(vac.name, 'Upd')
        self.assertEquals(vac.description, 'text text')

    def test_delete(self):
        vac = VacancyService.delete(1)
        self.assertEquals(vac, 'ok')