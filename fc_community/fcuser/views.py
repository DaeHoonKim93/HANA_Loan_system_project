from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import RegisterForm, LoginForm
from django.views.generic.edit import FormView
# from django.contrib.auth import authenticate, login
from django.db.models import Q
# 대훈코딩


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/fcuser/login'

    def form_valid(self, form):
        fcuser = Fcuser(
            emp_id=form.data.get('emp_id'),
            emp_name=form.data.get('emp_name'),
            password=make_password(form.data.get('password')),
            # level='user'
        )
        fcuser.save()

        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):  # 유효성 검사가 끝나고 로그인이 정상적으로 되면 들어오는 함수 !
        emp_id = form.data.get('emp_id')
        self.request.session['user'] = emp_id
        print("END")
        return super().form_valid(form)


def index(request):
    # print("INDEX session user : ", request.session.get('user'))
    # print(Fcuser)
    fcusers = Fcuser.objects.get(emp_id=request.session.get('user'))
    user = Fcuser.objects.filter(Q(emp_id=request.session.get('user')))
    emp_name = user.get().emp_name
    request.session['emp_name'] = emp_name
    print("HERE!!!")
    return render(request, 'home.html', {'fcusers': emp_name})


# def index(request):
#     return render(request, 'home.html',
#                   {'emp_name': request.session.get('user')})


def logout(request):
    if 'user' in request.session:
        del (request.session['user'])

    return redirect('/')


# 윤주코딩

# def home(request):
#     user_pk = request.session.get('user')

#     if user_pk:
#         fcuser = Fcuser.objects.get(pk=user_pk)
#         return HttpResponse(fcuser.emp_username)

#     return render(request, 'home.html')

# def logout(request):
#     if request.session.get("user"):
#         del(request.session['user'])

#     return redirect('/')

# def login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             request.session['user'] = form.emp_id
#             return redirect('/')  #홈페이지로 이동
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

# def sign_up(request):
#     if request.method == 'GET':
#         return render(request, 'sign_up.html')
#     elif request.method == 'POST':
#         # emp_name = request.POST['emp_name']
#         # password = request.POST['password']
#         # re_password = request.POST['re-password']

#         # 값이 안들어올수도있는경우를 대비해서 None으로 초기화
#         emp_name = request.POST.get('emp_name', None)
#         emp_id = request.POST.get('emp_id', None)
#         password = request.POST.get('password', None)
#         re_password = request.POST.get('re-password', None)

#         res_data = {}

#         if not (emp_name and emp_id and password and re_password):
#             res_data['error'] = "모든 값을 입력해야 합니다."

#         elif password != re_password:
#             res_data['error'] = "비밀번호가 다릅니다!"
# #            return HttpResponse("비밀번가 다릅니다!") // 이렇게 해주다가 dict를 만들어서 html로 보냄.
#         else:
#             fcuser = Fcuser(
#                 emp_name=emp_name,
#                 emp_id=emp_id,
#                 password=make_password(password)

#             )
#             fcuser.save()

#         return render(request, 'sign_up.html', res_data)
