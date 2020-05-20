from django.contrib import admin
from django.urls import path
from todo import views


urlpatterns = [
    path('admin/', admin.site.urls),

    #Authentication
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser,name='logoutuser'),

    #Todo items
    path('',views.home,name='home'),
    path('current/', views.currenttodos, name='currenttodos'),

]
