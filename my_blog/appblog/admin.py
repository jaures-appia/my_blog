from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('titre', 'status', 'date_add')
    search_fields = ('titre'),
    list_filter = ('status', 'date_add')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titre', 'status', 'date_add', 'categorie_id')
    search_fields = ('titre'),
    list_filter = ('status', 'date_add', 'categorie_id')# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class PostAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'date_add',
        'date_update',
        'status',
        'categorie_id',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'categorie_id',
        'id',
        'titre',
        'description',
        'date_add',
        'date_update',
        'status',
        'categorie_id',
    )


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'date_add',
        'date_update',
        'status',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'titre',
        'description',
        'date_add',
        'date_update',
        'status',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Post, PostAdmin)
_register(models.Categorie, CategorieAdmin)
