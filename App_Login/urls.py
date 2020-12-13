from django.urls import path
from App_Login import views

app_name = "App_Login"

urlpatterns = [
    path('account/signup/', views.sign_up, name='signup')
]
