from django.test import TestCase
from django.urls import reverse
from app.app_models.commonModels import News


class NewsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        News.objects.create(title='Test News1', text='This is a test news.')
        News.objects.create(title='Test News2', text='This is a test news.')

    def test_get(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.get('/news/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news.html')
        news = response.context[0]['news']
        self.assertEquals(len(news), 2)
        self.assertEquals(news[0]['title'], 'Test News1')

    def test_get_by_name(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.get(reverse('news'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news.html')
        news = response.context[0]['news']
        self.assertEquals(len(news), 2)
        self.assertEquals(news[0]['title'], 'Test News1')

    def test_post_invalid(self):
        response = self.client.post(reverse('news'))
        self.assertEquals(response.status_code, 302)

    def test_post_add(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('news'), data={'action': 'add'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news.html')
        self.assertIsNotNone(response.context[0]['form'])

    def test_post_save_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('news'), data={
                                    'action': 'save', 'title': 'Test title', 'text': 'Test text'})
        self.assertEquals(response.status_code, 302)
        news = News.objects.all()
        self.assertEquals(len(news), 3)
        self.assertEquals(news[2].title, 'Test title')

    def test_post_save_invalid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(reverse('news'), data={
                                    'action': 'save', 'title': '', 'text': 'Test text'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['form'].errors['title'], [
                          'This field is required.'])


class NewsDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        News.objects.create(title='Test News1', text='This is a test news.')
        News.objects.create(title='Test News2', text='This is a test news.')

    def test_get(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.get('/news/1')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news-detail.html')
        self.assertIsNotNone(response.context[0]['news'])
        self.assertEquals(response.context[0]['news'].title, 'Test News1')

    def test_post_invalid(self):
        response = self.client.post('/news/1')
        self.assertEquals(response.status_code, 302)

    def test_post_upd(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post('/news/1', {'action': 'upd'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news-detail.html')
        self.assertIsNotNone(response.context[0]['form'])

    def test_post_del(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post('/news/1', {'action': 'del'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(News.objects.count(), 1)

    def test_post_save_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post('/news/1', data={
                                    'action': 'save', 'title': 'Upd title', 'text': 'Upd text'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news-detail.html')
        self.assertIsNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['news'].title, 'Upd title')

    def test_post_save_invalid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post('/news/1', data={
                                    'action': 'save', 'title': '', 'text': 'Test text'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'news-detail.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['form'].errors['title'], [
                          'This field is required.'])
