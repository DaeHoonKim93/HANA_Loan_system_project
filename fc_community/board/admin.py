from django.contrib import admin
from .models import Worksheet, Process, LoanProcess, loan_product2, TodoList

# Register your models here.


class WorksheetAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name', 'loan_product',
                    'loan_amount', 'description', 'phone_number',
                    'register_date')


admin.site.register(Worksheet, WorksheetAdmin)


class ProcessAdmin(admin.ModelAdmin):
    list_display = ('loan_product', 'process_index', 'process_step')


admin.site.register(Process, ProcessAdmin)


class loan_product2Admin(admin.ModelAdmin):
    list_display = ('id', 'loan_product_name')


admin.site.register(loan_product2, loan_product2Admin)


class LoanProcessAdmin(admin.ModelAdmin):
    list_display = ('loan_product', 'loan_process_level', 'loan_process_name')


admin.site.register(LoanProcess, LoanProcessAdmin)


#######################################################################################
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('emp_name', 'content')


admin.site.register(TodoList, TodoListAdmin)
#######################################################################################