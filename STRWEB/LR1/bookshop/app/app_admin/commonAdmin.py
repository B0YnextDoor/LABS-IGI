from django.contrib import admin
from app.app_models.commonModels import AboutInfo, News, QA, Vacancy, SaleCode, CompanyPartner


@admin.register(AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'info', 'logo', 'video', 'history',
                    'requisites', 'certificate', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('info', 'logo', 'video', 'history',
                       'requisites', 'certificate', )
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


@admin.register(CompanyPartner)
class CompanyPartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'image', 'created_at', 'updated_at')
    list_filter = ('link', 'image', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('link', 'image')
        }),
        ('Object info', {'fields': ['created_at', 'updated_at']}))
