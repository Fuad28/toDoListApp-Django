from django.urls import path, include
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete,UserLoginView, Register
from django.contrib.auth.views import LogoutView


urlpatterns= [
    path('login/', UserLoginView.as_view(), name= 'base-login'), 
    path('logout/', LogoutView.as_view(next_page= 'base-login'), name= 'base-logout'), 
    path('register/', Register.as_view(), name= 'base-register'), 

     path('', TaskList.as_view(), name= 'base-tasklist'),
     path('task/<int:pk>/', TaskDetail.as_view(), name= 'base-taskdetails'),
     path('create-task/', TaskCreate.as_view(), name= 'base-taskcreate'),
     path('update-task/<int:pk>', TaskUpdate.as_view(), name= 'base-taskupdate'),
     path('delete-task/<int:pk>', TaskDelete.as_view(), name= 'base-taskdelete'),

]