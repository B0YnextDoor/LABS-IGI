from django.test import TestCase
from django.urls import reverse


class MainViewTest(TestCase):
    def test_get(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('main.html')
        self.assertFalse(response.context[0]['role'])

    def test_get_by_name(self):
        response = self.client.get(reverse('main'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('main.html')
        self.assertFalse(response.context[0]['role'])


class PolicyViewTest(TestCase):
    def test_get(self):
        response = self.client.get('/policy/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('policy.html')
        self.assertFalse(response.context[0]['role'])
        self.assertIsNotNone(response.context[0]['fact'])
        self.assertIsNotNone(response.context[0]['joke'])

    def test_get_by_name(self):
        response = self.client.get(reverse('policy'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('policy.html')
        self.assertFalse(response.context[0]['role'])
        self.assertIsNotNone(response.context[0]['fact'])
        self.assertIsNotNone(response.context[0]['joke'])
