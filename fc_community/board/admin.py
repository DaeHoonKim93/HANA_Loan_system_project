from django.contrib import admin
from .models import Worksheet, Process

# Register your models here.


class WorksheetAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name', 'loan_product',
                    'loan_amount', 'description', 'phone_number',
                    'register_date')


admin.site.register(Worksheet, WorksheetAdmin)


class ProcessAdmin(admin.ModelAdmin):
    list_display = ('loan_product', 'process_index', 'process_step')


admin.site.register(Process, ProcessAdmin)
