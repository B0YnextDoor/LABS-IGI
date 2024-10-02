from django.contrib import admin
from app.app_models.employeeModels import Employee, EmployeeInfo


class EmployeeInfoInline(admin.TabularInline):
    model = EmployeeInfo


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'password',
                    'is_admin', 'created_at', 'updated_at')
    list_filter = ('name', 'email', 'is_admin', 'created_at', 'updated_at')
    inlines = [EmployeeInfoInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'phone', 'email', 'password', 'is_admin')
        }),
        ('Object info', {'fields': ['created_at', 'updated_at']})
    )


@admin.register(EmployeeInfo)
class EmployeeInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_id', 'img', 'description',
                    'created_at', 'updated_at')
    list_filter = ['employee_id']
    fieldsets = (
        (None, {
            'fields': ('employee_id', 'description', 'img')
        }),
        ('Object info', {'fields': ['created_at', 'updated_at']})
    )
