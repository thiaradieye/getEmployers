from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_depart = ('name')

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_eemployer = ('first_name','last_name','phone_number','email','address','departement')


