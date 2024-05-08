from django.contrib import admin
from app.app_models.bookModels import Author, BookGenre, Book


class BookInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'created_at', 'updated_at')
    list_filter = ('surname', 'name', 'created_at', 'updated_at')
    inlines = [BookInline]
    fieldsets = (
        (None, {
            'fields': ('surname', 'name')
        }),
        ('Object info', {'fields': ['created_at', 'updated_at']})
    )


@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_filter = ('name', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ['name']
        }),
        ('Object info', {'fields': ['created_at', 'updated_at']})
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'genre', 'price',
                    'amount', 'created_at', 'updated_at')
    list_filter = ('title', 'author', 'genre', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'genre')
        }),
        ('Shop Info', {
            'fields': ('price', 'amount')
        }),
        ('Object info', {'fields': ['created_at', 'updated_at']})
    )
