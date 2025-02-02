from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


from .forms import LoginForm
from. import views

app_name = 'core' 

urlpatterns=[
    path('',views.index, name="index"),
    path('contact/',views.contact, name="contact"),
    path('signup/',views.signup, name='signup'),
    path('login/',LoginView.as_view(template_name= 'core/login.html', authentication_form=LoginForm), name='login'),
]