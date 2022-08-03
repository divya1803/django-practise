from django.contrib import admin
from . models import Details

@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    fields = ['name', 'email','phone_number']
    list_display = ['id','name','email','phone_number']


