from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import RegisterUserSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet
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

@api_view(['PUT'])
def uptade(request):
    userEdit= {
        'name': request.data.get('name'),
        'email': request.data.get('email'),
        'changeEmail': request.data.get('changeEmail') == 'Sim',
        'newEmail': request.data.get('newEmail'),
        'password': request.data.get('password'),
        'changeSenha': request.data.get('changeSenha') == 'Sim',
        'pais':request.data.get('pais'),
        'municipio':request.data.get('municipio'),
        'estado':request.data.get('estado'),
        'cep':request.data.get('cep'),
        'rua':request.data.get('rua'),
        'numero':request.data.get('numero'),
        'complemento':request.data.get('complemento'),
        'pis':request.data.get('pis'),
        'cpf':request.data.get('cpf'),
    }
    user = get_user_model().objects.filter(email=userEdit['email']).first()
    if user is None:
        raise exceptions.AuthenticationFailed('Usuário não encontrado!')
    user.name = userEdit['name']
    if(userEdit['changeEmail']):
        user.email = userEdit['newEmail']
    user.pais = userEdit['pais']
    user.municipio = userEdit['municipio']
    user.cep = userEdit['cep']
    user.estado = userEdit['estado']
    user.rua = userEdit['rua']
    user.numero = userEdit['numero']
    user.complemento = userEdit['complemento']
    user.cpf = userEdit['cpf']
    user.pis = userEdit['pis']
    if(userEdit['changeSenha']): 
        user.set_password(userEdit['password'])
    user.save()
    return Response({'mensagem': 'Edição concluida'})
class CurrentLoggedInUser(ModelViewSet):
    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    
    def retrieve(self, request, *args, **kwargs):
        user_profile = self.queryset.get(email=request.user.email)
        serializer = self.get_serializer(user_profile)
        return Response({'user':serializer.data})