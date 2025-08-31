from . import views
from django.urls import path

urlpatterns = [
    path('',views.task_list,name='task_list'),
    path('task/<int:pk>/',views.task_detail,name='task_detail'),
    path('create/',views.task_create,name='task_create'),
    path('task/<int:pk>/update/',views.task_update,name='task_update'),
    path('task/<int:pk>/delete/',views.task_delete,name='task_delete'),
]

