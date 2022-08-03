from django.contrib import admin
from .models import Employee
from .models import College
from . models import Car

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = [ 'name', 'phone_number']
    list_display = ['id', 'name', 'phone_number']

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    fields = ["name", "location"]

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    fields=["name", "price"]

