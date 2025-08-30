from . import views
from django.urls import path

urlpatterns = [
    path('',views.task_list,name='task_list'),
    path('task/<int:pk>/',views.task_detail,name='task_detail',)
]
