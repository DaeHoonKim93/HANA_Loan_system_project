from django.contrib import admin
from .models import Fcuser


# Register your models here.
class FcuserAmdin(admin.ModelAdmin):
    list_display = ('emp_name','password')

admin.site.register(Fcuser, FcuserAmdin);