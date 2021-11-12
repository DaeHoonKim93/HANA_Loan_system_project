from django.contrib import admin
from .models import Board


# Register your models here.
class BoardAmdin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Board, BoardAmdin)
