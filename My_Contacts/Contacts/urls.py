from django.urls import path
from . import views



urlpatterns = [
    path("", views.signin, name="signin"),
    path("signup.html",views.signup, name='signup'),
    path("signin.html",views.signin,name="signin"),
    path("phonebook.html",views.phonebook,name="phonebook"),
    path('dispaly.html',views.display,name='dispally')
]
