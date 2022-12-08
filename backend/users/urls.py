from django.urls import path
from .views import RegisterUserView, login

urlpatterns = [
    path('login', login),
    path('cadastrar', RegisterUserView.as_view(), name='cadastrar')
]