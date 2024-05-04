from django.contrib import admin
from .models import products

@admin.register(products)
class productAdmin(admin.ModelAdmin):
    list_display = ("type","name","description","price","image")