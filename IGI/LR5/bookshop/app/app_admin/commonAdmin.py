from django.contrib import admin
from app.app_models.commonModels import AboutInfo, News, QA, Vacancy, SaleCode


@admin.register(AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'info', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ['info']
        }),
        ('Object info', {'fields': ['created_at', 'updated_at']})
    )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'img', 'created_at', 'updated_at')
    list_filter = ('title', 'created_at', 'img', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'img')
        }),
        ('Object info', {'fields': ['created_at', 'updated_at']})
    )


@admin.register(QA)
class QAAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'created_at', 'updated_at')
    list_filter = ('question', 'answer', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('question', 'answer')
        }),
        ('Object info', {'fields': ['created_at', 'updated_at']})
    )


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Object info', {'fields': ['created_at', 'updated_at']})
    )


@admin.register(SaleCode)
class SaleCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'is_active', 'created_at', 'updated_at')
    list_filter = ('code', 'is_active', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('code', 'is_active')
        }),
        ('Object info', {'fields': ['created_at', 'updated_at']})
    )
