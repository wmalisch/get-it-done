from django.contrib import admin
from django.urls import path
from todo import views


urlpatterns = [
    path('admin/', admin.site.urls),

    #Authentication
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser,name='logoutuser'),
    path('login', views.loginuser,name='loginuser'),

    #Todo items
    path('',views.home,name='home'),
    path('create/', views.createtodo,name='createtodo'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('todo/<int:todo_pk>',views.viewtodo,name='viewtodo'),
    path('todo/<int:todo_pk>/complete',views.completetodo,name='completetodo'),
    path('todo/<int:todo_pk>/delete',views.deletetodo,name='deletetodo'),
    path('completed/',views.completedtodos,name='completedtodos'),
    

]
