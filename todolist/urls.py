from django.urls import path
from todolist.views import show_task, login_user, register, logout_user, create_task

app_name = 'todolist'

urlpatterns = [
    path('', show_task, name='show_task'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task')
]