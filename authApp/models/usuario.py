from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_usuario(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superusuario(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_usuario(
        username=username,
        password=password,
    )
        user.is_admin = True
        user.save(using=self._db)
        return user
        
class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True, unique= True)
    username=models.CharField('Username', max_length=15,unique = True)
    usuario_nombre = models.CharField('Nombre', max_length = 45, unique=False)
    usuario_telefono = models.CharField('Telefono', max_length = 10, unique=True)
    usuario_tipo_id = models.CharField('Tipo_id', max_length = 20, unique=False)
    usuario_numero_id = models.IntegerField('Numero_id', unique=True)
    usuario_ciudad = models.CharField('Ciudad', max_length = 10, unique=False)
    usuario_direccion = models.CharField('Direccion', max_length = 50, unique=False)
    password = models.CharField('Password', max_length = 256)
    usuario_email = models.EmailField('Email', max_length = 50, unique=True)
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    objects = UserManager()
    USERNAME_FIELD = 'username'
