from django.urls import path
from todolist.views import show_task, login_user, register, logout_user, create_task, finished_task, delete_task, get_todolist_json, add_todolist_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_task, name='show_task'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('finished_task/<int:id>', finished_task, name='finished_task'),
    path('delete_task/<int:id>', delete_task, name='delete_task'),
    path('json/', get_todolist_json , name='get_todolist_json'),
    path('add/', add_todolist_ajax , name='add_todolist_ajax'),
]   