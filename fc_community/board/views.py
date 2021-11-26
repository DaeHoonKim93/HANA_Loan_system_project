from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Worksheet
from fcuser.models import Fcuser
from fcuser.views import index
from .forms import RegisterForm

# Create your views here.


def Worksheet_Create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid(form):
            worksheet = Worksheet(
                customer_id=form.data.get('customer_id'),
                customer_name=form.data.get('customer_name'),
                loan_product=form.data.get('loan_product'),
                loan_amount=form.data.get('loan_amount'),
                description=form.data.get('description'),
                phone_number=form.data.get('phone_number'),
                #   지훈 코딩
                loan_start_date=form.data.get('loan_start_date'))

            worksheet.save()
    else:
        form = RegisterForm()
    context = {'worksheet': worksheet, 'form': form}
    return render(request, 'worksheet.html', context)


class WorksheetList(ListView):
    model = Worksheet
    template_name = 'Worksheet.html'
    context_object_name = 'Worksheet_list'


class WorksheetCreate(FormView):
    template_name = 'register_work.html'
    form_class = RegisterForm
    success_url = '/worksheet/'

    def form_valid(self, form):
        print("user : ", self.request.session.get('user'))
        print("emp_name : ", self.request.session.get('emp_name'))
        worksheet = Worksheet(
            customer_id=form.data.get('customer_id'),
            customer_name=form.data.get('customer_name'),
            loan_product=form.data.get('loan_product'),
            loan_amount=form.data.get('loan_amount'),
            description=form.data.get('description'),
            phone_number=form.data.get('phone_number'),
            #   지훈 코딩
            loan_start_date=form.data.get('loan_start_date'),
            emp_name=self.request.session.get('emp_name'))

        worksheet.save()
        return super().form_valid(form)
