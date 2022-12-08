from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required= True,
        validators=[UniqueValidator(queryset=get_user_model().objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = get_user_model()
        fields = ('email','name','password','pais','estado','municipio','cep','rua','numero','complemento','cpf','pis')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
            'email' : {'required': True},
            'name': {'required': True},
            'pais': {'required': True},
            'estado': {'required': True},
            'municipio': {'required': True},
            'cep': {'required': True},
            'rua': {'required': True},
            'numero': {'required': True},
            'cpf': {'required': True},
            'pis': {'required': True},
        }
    
    def create(self, validated_data):
        user = self.Meta.model.objects.create(
            name= validated_data['name'],
            email= validated_data['email'],
            pais = validated_data['pais'],
            estado = validated_data['estado'],
            municipio = validated_data['municipio'],
            cep = validated_data['cep'],
            rua = validated_data['rua'],
            numero = validated_data['numero'],
            complemento = validated_data['complemento'],
            cpf= validated_data['cpf'],
            pis= validated_data['pis'],
        )
        
        user.set_password(validate_password('password'))
        user.save()
        
        return user