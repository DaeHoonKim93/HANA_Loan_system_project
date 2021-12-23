from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.views.generic.edit import FormView

from .models import Fcuser
from board.models import Worksheet
from .forms import RegisterForm, LoginForm

from datetime import datetime


# 직원정보 등록
class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/fcuser/login'

    def form_valid(self, form):
        fcuser = Fcuser(emp_id=form.data.get('emp_id'),
                        emp_name=form.data.get('emp_name'),
                        password=make_password(form.data.get('password')))
        fcuser.save()

        return super().form_valid(form)


# 로그인 기능
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):  # 유효성 검사가 끝나고 로그인이 정상적으로 되면 들어오는 함수
        emp_id = form.data.get('emp_id')
        self.request.session['user'] = emp_id
        return super().form_valid(form)


#로그아웃
def logout(request):
    if 'user' in request.session:
        del (request.session['user'])

    return redirect('/')
