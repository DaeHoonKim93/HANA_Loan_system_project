
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.board_list),
    path('write/', views.board_write),
    path('work-registration/', views.work_registration)
]
