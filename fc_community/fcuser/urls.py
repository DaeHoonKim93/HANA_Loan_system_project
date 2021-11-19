
from django.urls import path
from . import views
# from fcuser.views import LoginView
from fcuser.views import  RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),  # class는 as_view()써줘야함
    path('login/', LoginView.as_view()),
    path('logout/', views.logout, name = 'logout'),
]
