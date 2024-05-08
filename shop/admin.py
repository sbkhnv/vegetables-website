from django.contrib import admin
from .models import Products

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("type","name","description","price","image")