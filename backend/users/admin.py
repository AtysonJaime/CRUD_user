from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ('email','name','cep','cpf','pis', 'is_staff','is_admin')
    list_filter = ('is_admin',)
    
    fieldsets = (
        (None, {'fields':('email','name','password','pais','estado','municipio','cep','rua','numero','complemento','cpf','pis')}),
        ('Permissions',{'fields':('is_admin','is_staff','is_active')}),
    )

    search_fields = ('email','name','cpf','pis',)
    ordering = ('email', 'name',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)