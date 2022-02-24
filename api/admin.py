import email
from django.contrib import admin

from . import models

@admin.register(models.User)
class UsereAdmin(admin.ModelAdmin):
    list_display = ('name', 'email') 
    list_display_links = ('email',)

@admin.register(models.Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = ('code', 'perday') 
    list_display_links = ('code',)

@admin.register(models.Concorso)
class ConcorsoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('name',)

@admin.register(models.Winer)
class WinerAdmin(admin.ModelAdmin):
    list_display = ('id', 'winner') 
    list_display_links = ('winner',)



