"""fc_community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from board.views import index, charts, WorksheetList, WorksheetCreate, Total_worksheetList, VirtualBankSystem, Workdetail, TodoList_list, addTodoView, deleteTodoView, WorksheetUpdate, WorksheetDelete, Howto_Use

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fcuser/', include('fcuser.urls')),
    path('', index, name='home'),
    path('charts/', charts, name='charts'),
    path('worksheet/', WorksheetList, name='worksheet'),
    path('totalworksheet/', Total_worksheetList, name='totalworksheet'),
    path('worksheet/create/',
         WorksheetCreate.as_view(),
         name='worksheetcreate'),
    path('virtualbanksystem/', VirtualBankSystem, name='virtualbanksystem'),
    path('worksheet/detail/<int:pk>/', Workdetail.as_view()),
    path('todo_list/', TodoList_list, name='TodoList'),
    path('addTodoItem/', addTodoView, name='addTodoView '),
    path('deleteTodoItem/<int:i>/', deleteTodoView, name='deleteTodoView'),
    path('worksheet/update/<int:pk>/',
         WorksheetUpdate.as_view(),
         name='update'),
    path('worksheet/delete/<int:pk>', WorksheetDelete.as_view(),
         name='delete'),
    path('howto_use/', Howto_Use, name='howto_use')
]
