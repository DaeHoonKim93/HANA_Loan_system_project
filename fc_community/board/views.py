from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponseRedirect

from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, UpdateView, DeleteView

from .models import Worksheet, Process, TodoList
from fcuser.models import Fcuser
from .forms import RegisterForm
from datetime import datetime
from django.core.paginator import Paginator

from django.db import connection
from .decorators import is_login


class WorksheetDelete(DeleteView):
    model = Worksheet
    template_name = 'work_delete.html'
    success_url = '/worksheet'


class WorksheetUpdate(UpdateView):
    model = Worksheet
    fields = [
        'customer_id', 'customer_name', 'phone_number', 'loan_product',
        'loan_amount', 'loan_start_date', 'description'
    ]
    template_name = 'work_update.html'
    context_object_name = 'worksheet'  #1
    success_url = '/worksheet'  #3

    # #get object
    # def get_object(self):
    #     review = get_object_or_404(Review, pk=self.kwargs['pk']) #4

    #     return review


def tables(request):
    return render(request, 'tables.html')


def index(request):
    if request.session.get('user') == None:
        return redirect('fcuser/login/')
    else:
        fcusers = Fcuser.objects.get(emp_id=request.session.get('user'))
        user = Fcuser.objects.filter(emp_id=request.session.get('user'))
        emp_name = user.get().emp_name  #로그인된 user
        request.session['emp_name'] = emp_name

        cursor = connection.cursor()
        strSql = "select A.customer_id, A.customer_name, A.loan_product, A.loan_amount, A.loan_start_date  , C.loan_process_name, A.emp_name from WorkSheet as A Left OUTER join (select A.loan_product_name, B.loan_process_level, B.loan_process_name from loan_product2 as A inner join loan_process as B on a.id = b.loan_product_id) as C on a.loan_product = C.loan_product_name WHERE A.current_process_id = C.loan_process_level AND A.loan_start_date - curdate() < 5 AND A.loan_start_date - curdate() > 0"
        result = cursor.execute(strSql)
        works = cursor.fetchall()
        connection.commit()
        within_5days_work = []
        # print("works!!", works)
        for data in works:
            row = {
                'emp_name': data[6],
                'customer_id': data[0],
                'customer_name': data[1],
                'loan_product': data[2],
                'loan_amount': data[3],
                'loan_start_date': data[4],
                'loan_process_name': data[5]
            }
            within_5days_work.append(row)

        TodoList_list = TodoList.objects.all()

        return render(
            request, 'home.html', {
                'fcusers': emp_name,
                'within_5days_work': within_5days_work,
                'TodoList_list': TodoList_list
            })


@is_login
def VirtualBankSystem(request):

    Worksheet_list = Worksheet.objects.all()

    if request.method == 'POST':
        lst_id = request.POST.getlist('id')

        for i in lst_id:

            next_process_level = Worksheet.objects.get(
                id=int(i)).current_process_id + 1

            Worksheet.objects.filter(id=int(i)).update(
                current_process_id=next_process_level)

        return redirect('/virtualbanksystem')

    return render(request, 'VirtualBankSystem.html',
                  {'Worksheet_list': Worksheet_list})


@is_login
def WorksheetList(request):

    cursor = connection.cursor()
    # strSql = "select A.* , B.process_step from WorkSheet as A Left OUTER join Process as B on a.loan_product = b.loan_product WHERE A.current_process_id = B.process_index"
    strSql = "select A.* , C.loan_process_name from WorkSheet as A Left OUTER join (select A.loan_product_name, B.loan_process_level, B.loan_process_name from loan_product2 as A inner join loan_process as B on a.id = b.loan_product_id) as C on a.loan_product = C.loan_product_name WHERE A.current_process_id = C.loan_process_level"
    result = cursor.execute(strSql)
    works = cursor.fetchall()
    connection.commit()
    datas = []
    # print("workszzz", works)
    for data in works:
        if data[5] == 'HF 주택신용보증 전세대출':
            prog = data[11] / 5 * 100
        else:
            prog = data[11] / 6 * 100
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
            'process_step': data[12],
            'progress': prog
        }
        datas.append(row)

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

    page = request.GET.get('page', '1')  # 페이지

    # 조회
    # work_list = Worksheet.objects.order_by('-id')
    # print("work_list!!", work_list)
    # print("datas", datas)
    # 페이징처리
    paginator = Paginator(datas, 5)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    return render(request, 'Worksheet.html', {
        'datas': datas,
        'work_list': page_obj
    })

    # print(Worksheet_list)
    # emp_name = user.get().emp_name  #로그인된 user
    # request.session['emp_name'] = emp_name
    # print("HERE!!!")


@is_login
def Total_worksheetList(request):

    cursor = connection.cursor()
    # strSql = "select A.* , B.process_step from WorkSheet as A Left OUTER join Process as B on a.loan_product = b.loan_product WHERE A.current_process_id = B.process_index"
    strSql = "select A.* , C.loan_process_name from WorkSheet as A Left OUTER join (select A.loan_product_name, B.loan_process_level, B.loan_process_name from loan_product2 as A inner join loan_process as B on a.id = b.loan_product_id) as C on a.loan_product = C.loan_product_name WHERE A.current_process_id = C.loan_process_level"
    result = cursor.execute(strSql)
    works = cursor.fetchall()
    connection.commit()
    datas = []
    # print("works!!!", works)
    for data in works:
        if data[5] == 'HF 주택신용보증 전세대출':
            prog = data[11] / 5 * 100
        else:
            prog = data[11] / 6 * 100
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
            'process_step': data[12],
            'progress': prog
        }
        datas.append(row)
    # print(datas)

    # connection.close()

    # user = Worksheet.objects.filter(
    #     Q(emp_id=request.session.get('user')))  # where절

    # page = request.GET.get('page', '1')  # 페이지

    # # 조회
    # work_list = Worksheet.objects.order_by('-id')
    # print("dd", type(work_list))
    # print("dddd", type(datas))

    # # print("work_list!!", work_list)
    # # print("datas", datas)
    # # 페이징처리
    # paginator = Paginator(datas, 10)  # 페이지당 10개씩 보여주기

    # page_obj = paginator.get_page(page)
    return render(request, 'Total_Worksheet.html', {'datas': datas})


class WorksheetCreate(FormView):
    template_name = 'register_work.html'
    form_class = RegisterForm
    success_url = '/worksheet/'

    def form_valid(self, form):
        # print("user : ", self.request.session.get('user'))
        # print("emp_name : ", self.request.session.get('emp_name'))
        worksheet = Worksheet(
            customer_id=form.data.get('customer_id'),
            customer_name=form.data.get('customer_name'),
            loan_product=form.data.get('loan_product'),
            loan_amount=form.data.get('loan_amount'),
            description=form.data.get('description'),
            phone_number=form.data.get('phone_number'),
            #   지훈 코딩
            loan_start_date=form.data.get('loan_start_date'),
            emp_name=self.request.session.get('emp_name'),
            loan_condition=form.data.get('loan_condition'))
        worksheet.save()
        return super().form_valid(form)


class Workdetail(DetailView):
    template_name = 'work_detail.html'
    queryset = Worksheet.objects.all()
    context_object_name = 'Workdetail'


def charts(request):
    #sql 리스트롤
    #쿼리를짜서 그룹바이 emp_name select count(*)

    # 1. 직원별 대출 신규 건수를 확인하는 코드
    cursor = connection.cursor()
    strSql = "select emp_name, count(*) from worksheet group by emp_name;"
    result = cursor.execute(strSql)
    emp_count_lst = cursor.fetchall()
    connection.commit()
    # print('emp_count_lst', emp_count_lst)
    data_lst = []
    name_lst = []
    for i in range(len(emp_count_lst)):
        data_lst.append(emp_count_lst[i][1])
        name_lst.append(emp_count_lst[i][0])
    # print('data_list',data_lst)
    # print('name_list',name_lst)

# 2. 대출 총 건수의 합을 구하는 코드
    strSql_2 = "select count(*) from worksheet;"
    result_2 = cursor.execute(strSql_2)
    total_count = cursor.fetchall()
    connection.commit()
    data_lst.append(total_count[0][0])
    # print(total_count[0][0])

    # 3. 직원별 대출 금액 합을 구하는 코드
    strSql_3 = "select emp_name, round((sum(loan_amount)/100000000),2) from worksheet group by emp_name;"
    result_3 = cursor.execute(strSql_3)
    amount_lst = cursor.fetchall()
    connection.commit()
    individual_amount_lst = []
    for i in range(len(amount_lst)):
        individual_amount_lst.append(int(amount_lst[i][1]))
    #     print('bbbbbb', individual_amount_lst)
    # print('aaaaaaa', individual_amount_lst)

# 4. 대출 총 금액의 합을 구하는 코드
# strSql_4 = "select sum(loan_amount) from worksheet;"
# result_4 = cursor.execute(strSql_4)
# total_amount = cursor.fetchall()
# connection.commit()
# individual_amount_lst.append(float(individual_amount_lst[0][0]))
# print('asdasdasdasd', total_amount[0][0])

# 5. 상품별 대출 신규 건수를 확인하는 코드
    strSql_5 = "select loan_product, count(*) from worksheet group by loan_product;"
    result = cursor.execute(strSql_5)
    product_count = cursor.fetchall()
    connection.commit()
    product_lst = []
    for i in range(len(product_count)):
        product_lst.append(product_count[i][1])
    print('aaaaaa', product_lst)

    # 5. 모든 대출 신규 건수를 확인하는 코드
    strSql_6 = "SELECT DATE_FORMAT(loan_start_date, '%Y-%m') as date, count(*) FROM worksheet GROUP BY DATE_FORMAT(loan_start_date, '%Y-%m') ORDER BY date ASC;"
    result = cursor.execute(strSql_6)
    month_total = cursor.fetchall()
    connection.commit()
    month_lst = []
    for i in range(len(month_total)):
        month_lst.append(month_total[i][1])
    print('aaaaaa', month_lst)

    return render(
        request, 'charts.html', {
            'data_lst': data_lst,
            'name_lst': name_lst,
            'individual_amount_lst': individual_amount_lst,
            'product_lst': product_lst,
            'month_lst': month_lst
        })


#윤주#########################################################################################


def TodoList_list(request):
    all_todo_items = TodoList.objects.all()
    return render(request, 'todo_list.html',
                  {'all_todo_items': all_todo_items})


def addTodoView(request):
    x = request.POST['content']
    new_item = TodoList(content=x)
    new_item.save()
    return HttpResponseRedirect('/todo_list/')


def deleteTodoView(request, i):
    y = TodoList.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todo_list/')