from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from .serializers import RegisterUserSerializer
from rest_framework.decorators import api_view
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.reverse import reverse
import requests


# Create your views here.

class RegisterUserView(CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

@api_view(['POST'])
def login(request):
    login = request.data.get('login')
    password = request.data.get('password');
    
    user = get_user_model().objects.filter(email=login).first()
    if (user) is None:
        user = get_user_model().objects.filter(cpf=login).first()
        if (user) is None:
            user = get_user_model().objects.filter(pis=login).first()
            if user is None:
                raise exceptions.AuthenticationFailed('Usuário não encontrado!')

    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Senha incorreta!')
    
    response = Response()
    
    requestToken = {'email':[user.email],'password':[password]}
    
    token_endpoint = reverse(viewname='token_obtain_pair', request=request)
    tokens = requests.post(token_endpoint, data=requestToken).json()
    
    response.data = {
        'access_token':tokens.get('access'),
        'refresh_token':tokens.get('refresh'),
        'email': user.email
    }
    
    return response