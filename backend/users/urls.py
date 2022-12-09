from django.urls import path
from .views import RegisterUserView, login, uptade, CurrentLoggedInUser

urlpatterns = [
    path('login', login),
    path('cadastrar', RegisterUserView.as_view(), name='cadastrar'),
    path("user", CurrentLoggedInUser.as_view({'get':'retrieve'}),name='current_user'),
    path('update', uptade)
]