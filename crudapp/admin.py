from django.contrib import admin
from crudapp.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'ename', 'eno', 'eaddress', 'esal']


# Register your models here.

admin.site.register(Employee, EmployeeAdmin)
