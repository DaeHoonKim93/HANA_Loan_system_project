from django.contrib import admin
from .models import Worksheet

# Register your models here.


class WorksheetAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'loan_amount')


admin.site.register(Worksheet, WorksheetAdmin)
