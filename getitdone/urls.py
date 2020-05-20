from django.contrib import admin
from django.urls import path
from todo import views


urlpatterns = [
    path('admin/', admin.site.urls),

    #Authentication
    path('signup/', views.signupuser, name='signupuser'),

    #Todo items
    path('current/', views.currenttodos, name='currenttodos'),

]
