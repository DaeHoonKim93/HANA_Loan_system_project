from django.contrib import admin
from .models import Worksheet, LoanProcess, LoanProduct, TodoList


class WorksheetAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name', 'loan_product',
                    'loan_amount', 'description', 'phone_number',
                    'register_date')


admin.site.register(Worksheet, WorksheetAdmin)


class LoanProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'loan_product_name')


admin.site.register(LoanProduct, LoanProductAdmin)


class LoanProcessAdmin(admin.ModelAdmin):
    list_display = ('loan_product', 'loan_process_level', 'loan_process_name')


admin.site.register(LoanProcess, LoanProcessAdmin)


#######################################################################################
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('emp_name', 'content')


admin.site.register(TodoList, TodoListAdmin)
#######################################################################################