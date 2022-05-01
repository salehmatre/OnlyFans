from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models import CharField

from .decorators import validate_user

# Create your models here.


class UserManager(BaseUserManager):
    """Моделька Менеджера по 1 методу"""

    use_in_migrations = True

    @validate_user
    def create_user(self, email, username, password):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    @validate_user
    def create_superuser(self, email, username, password):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    "Моделька пользователя по 1 методу"

    # сделал ночью на будущее, если вдруг наши фронты успеют, текущая дата 1:38

    username = models.CharField(max_length=122)
    email = models.EmailField(('Email'), unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def __str__(self) -> CharField:
        return self.username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'