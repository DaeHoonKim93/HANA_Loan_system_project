from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Worksheet, Process
from fcuser.models import Fcuser
from fcuser.views import index
from .forms import RegisterForm

from django.db import connection

# Create your views here


def VirtualBankSystem(request):

    Worksheet_list = Worksheet.objects.all()
    # print(type(Worksheet_list))
    # var_id = 3
    # Process_data = Process.objects.filter(id=var_id)
    # for work in Worksheet_list:
    #     # print('zz', type(work))
    #     break
    # a = Process_data[0]
    # print(a.process_step)
    # b = a.process_step
    if request.method == 'POST':
        lst_id = request.POST.getlist('id')

        for i in lst_id:

            next_process_level = Worksheet.objects.get(
                id=int(i)).current_process_id + 1

            Worksheet.objects.filter(id=int(i)).update(
                current_process_id=next_process_level)

        # cursor = connection.cursor()
        # strSql = "UPDATE Worksheet set current_process_id = current_process_id + 1"
        # result = cursor.execute(strSql)
        # id_process = cursor.fetchall()
        # connection.commit()

        return redirect('/virtualbanksystem')

    return render(request, 'VirtualBankSystem.html',
                  {'Worksheet_list': Worksheet_list})


def WorksheetList(request):

    cursor = connection.cursor()
    # strSql = "select A.* , B.process_step from WorkSheet as A Left OUTER join Process as B on a.loan_product = b.loan_product WHERE A.current_process_id = B.process_index"
    strSql = "select A.* , C.loan_process_name from WorkSheet as A Left OUTER join (select A.loan_product_name, B.loan_process_level, B.loan_process_name from loan_product2 as A inner join loan_process as B on a.id = b.loan_product_id) as C on a.loan_product = C.loan_product_name WHERE A.current_process_id = C.loan_process_level"
    result = cursor.execute(strSql)
    works = cursor.fetchall()
    connection.commit()
    datas = []
    for data in works:
        print(data[1])
        row = {
            'id': data[0],
            'emp_name': data[1],
            'customer_id': data[2],
            'customer_name': data[3],
            'loan_start_date': data[4],
            'loan_product': data[5],
            'loan_amount': data[6],
            'loan_condition': data[7],
            'description': data[8],
            'phone_number': data[9],
            'register_date': data[10],
            'current_process_id': data[11],
            'process_step': data[12]
        }
        datas.append(row)
    # print(datas)

    # strSql2 = "SELECT process_step FROM Process"
    # result = cursor.execute(strSql2)
    # proc = cursor.fetchall()
    # connection.commit()
    # connection.close()

    # user = Worksheet.objects.filter(
    #     Q(emp_id=request.session.get('user')))  # where절

    Worksheet_list = Worksheet.objects.all()
    # print(type(Worksheet_list))
    var_id = 3
    Process_data = Process.objects.filter(id=var_id)
    # for work in Worksheet_list:
    #     # print('zz', type(work))
    #     break
    # a = Process_data[0]
    # print(a.process_step)
    # b = a.process_step
    return render(request, 'Worksheet.html', {
        'datas': datas,
        'Worksheet_list': Worksheet_list
    })

    # print(Worksheet_list)
    # emp_name = user.get().emp_name  #로그인된 user
    # request.session['emp_name'] = emp_name
    # print("HERE!!!")


# class WorksheetList(ListView):
#     model = Worksheet  # 데이터 ,, WorkSheet, Process
#     template_name = 'Worksheet.html'
#     context_object_name = 'Worksheet_list'


class Total_worksheetList(ListView):
    model = Worksheet
    template_name = 'Total_worksheet.html'
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
        # loan_condition=form.data.get('loan_condition'))
        worksheet.save()
        return super().form_valid(form)


class Workdetail(DetailView):
    template_name = 'work_detail.html'
    queryset = Worksheet.objects.all()
    context_object_name = 'Workdetail'


def charts(request):
    return render(request, 'charts.html')


# def index(request):
#     return render(request, 'home.html',
#                   {'emp_name': request.session.get('user')})
