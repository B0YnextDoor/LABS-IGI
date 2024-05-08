from app.app_models.baseModel import models, BaseModel
from django.urls import reverse


class Author(BaseModel):
    name = models.TextField(help_text='Author\'s name')
    surname = models.TextField(help_text='Author\'s surname')

    class Meta:
        db_table = 'authors_table'
        ordering = ['surname']

    def __str__(self) -> str:
        return f'{self.id} {self.surname} {self.name} {self.created_at} {self.updated_at}'


class BookGenre(BaseModel):
    name = models.TextField(unique=True, help_text='Genre\'s name')

    class Meta:
        db_table = 'genres_table'
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.created_at} {self.updated_at}'


class Book(BaseModel):
    title = models.TextField(help_text='Book\'s title')
    price = models.FloatField(help_text='Book\'s price')
    amount = models.PositiveIntegerField(
        help_text='Amount of copies in the shop')
    genre = models.ForeignKey(
        BookGenre, on_delete=models.SET_DEFAULT, default='Роман')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books_table'
        ordering = ['-price']

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return f'{self.id} {self.title} {self.author} {self.genre} {self.price} {self.amount} {self.created_at} \
{self.updated_at}'
