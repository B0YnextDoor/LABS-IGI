from django.test import TestCase
from django.urls import reverse
from app.app_models import bookModels as bm, customerModel as cm, employeeModels as em


class BookViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cm.Customer.objects.create(
            name='Test Customer', phone='+375291111111', email='test@customer.com', password='Testpassword1')
        em.Employee.objects.create(
            name='Test Employee', phone='+375291111111', email='test@employee.com', password='Testpassword1', is_admin=True)
        genre = bm.BookGenre.objects.create(name='Fiction')
        author = bm.Author.objects.create(name='John', surname='Doe')
        bm.Book.objects.create(
            title='Test Book', price=19.99, amount=10, genre=genre, author=author)

    def test_get(self):
        session = self.client.session
        session['role'] = 'usr'
        session.save()
        response = self.client.get('/books/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books.html')
        query_set = response.context[0]['book_list']
        self.assertIsNotNone(query_set)
        self.assertEquals(len(query_set), 1)

    def test_get_by_name(self):
        session = self.client.session
        session['role'] = 'usr'
        session.save()
        response = self.client.get(reverse('catalog'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books.html')
        query_set = response.context[0]['book_list']
        self.assertIsNotNone(query_set)
        self.assertEquals(len(query_set), 1)

    def test_get_with_query(self):
        session = self.client.session
        session['role'] = 'usr'
        session.save()
        response = self.client.get(reverse('catalog'), data={
                                   'search': 'Dinosaurus'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books.html')
        self.assertEquals(response.context[0]['book_list'], [])

    def test_post_customer_valid(self):
        session = self.client.session
        session['role'] = 'usr'
        session.save()
        response = self.client.post(
            reverse('catalog'), data={'sort_by': 'amount'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books.html')
        query_set = response.context[0]['book_list']
        self.assertIsNotNone(query_set)
        self.assertEquals(len(query_set), 1)

    def test_post_customer_invalid(self):
        session = self.client.session
        session['role'] = 'usr'
        session.save()
        response = self.client.post(
            reverse('catalog'), data={'action': 'create'})
        self.assertEquals(response.status_code, 302)

    def test_post_admin_create(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(
            reverse('catalog'), data={'action': 'create'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books.html')
        self.assertIsNotNone(response.context[0]['form'])

    def test_post_admin_save_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(
            reverse('catalog'), data={'action': 'save', 'title': 'New book', 'price': 24.5, 'amount': 3, 'genre': '1', 'author': '1'})
        self.assertEquals(response.status_code, 302)

    def test_post_admin_save_invalid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(
            reverse('catalog'), data={'action': 'save', 'title': '', 'price': 24.5, 'amount': 3, 'genre': '1', 'author': '1'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context[0]['form'].errors['title'], [
                          'This field is required.'])


class BookDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cm.Customer.objects.create(
            name='Test Customer', phone='+375291111111', email='test@customer.com', password='Testpassword1')
        em.Employee.objects.create(
            name='Test Employee', phone='+375291111111', email='test@employee.com', password='Testpassword1', is_admin=True)
        genre = bm.BookGenre.objects.create(name='Fiction')
        author = bm.Author.objects.create(name='John', surname='Doe')
        bm.Book.objects.create(
            title='Test Book', price=19.99, amount=10, genre=genre, author=author)

    def test_get_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.get('/books/1')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book-detail.html')
        self.assertIsNotNone(response.context[0]['book'])

    def test_post_invalid(self):
        session = self.client.session
        session['role'] = 'usr'
        session.save()
        response = self.client.post('/books/1', {'action': 'edit'})
        self.assertEquals(response.status_code, 302)

    def test_post_edit(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post('/books/1', {'action': 'edit'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book-detail.html')
        self.assertIsNotNone(response.context[0]['form'])

    def test_post_del(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post('/books/1', {'action': 'del'})
        self.assertEquals(response.status_code, 302)

    def test_post_save_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(
            '/books/1', {'action': 'save', 'title': 'New title', 'price': 19.99, 'amount': 10, 'genre': '1', 'author': '1'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book-detail.html')
        self.assertIsNone(response.context[0]['form'])
        self.assertIsNotNone(response.context[0]['book'])
        self.assertEquals(response.context[0]['book'].title, 'New title')

    def test_post_save_invalid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.post(
            '/books/1', {'action': 'save', 'title': 'New title', 'price': -10, 'amount': 10, 'genre': '1', 'author': '1'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book-detail.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['form'].non_field_errors()[
                          0], 'Wrong price format')
