from django.urls import path
from .views import RegisterUserView

urlpatterns = [
    path('cadastrar', RegisterUserView.as_view(), name='cadastrar')
]