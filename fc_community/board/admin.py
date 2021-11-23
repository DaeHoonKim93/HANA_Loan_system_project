from django.contrib import admin
from .models import Worksheet

# Register your models here.


class WorksheetAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name', 'loan_product',
                    'loan_amount', 'description', 'phone_number',
                    'register_date')


admin.site.register(Worksheet, WorksheetAdmin)
