from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.DoTitleView.as_view(), name='home'),
    path('todolist/<int:pk>', views.DoTitleDetail.as_view(), name ='detail'),
]
