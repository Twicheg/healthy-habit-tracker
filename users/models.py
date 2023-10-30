from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    tg_chat_id = models.BigIntegerField(verbose_name="Chat_id пользователя", null=True, blank=True)
    tg_username = models.CharField(max_length=50, verbose_name="телеграм юзернейм")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email},{self.tg_username},{self.tg_chat_id}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('id',)
