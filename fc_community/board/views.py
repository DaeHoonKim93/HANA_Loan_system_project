from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Worksheet
from .forms import RegisterForm
# Create your views here.


class WorksheetList(ListView):
    model = Worksheet
    template_name = 'Worksheet.html'
    context_object_name = 'Worksheet_list'


class WorksheetCreate(FormView):
    template_name = 'register_work.html'
    form_class = RegisterForm
    success_url = '/worksheet/'

    def form_valid(self, form):
        worksheet = Worksheet(customer_id=form.data.get('customer_id'),
                              customer_name=form.data.get('customer_name'),
                              loan_product=form.data.get('loan_product'),
                              loan_amount=form.data.get('loan_amount'),
                              description=form.data.get('description'),
                              phone_number=form.data.get('phone_number'))
        worksheet.save()
        return super().form_valid(form)
