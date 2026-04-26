from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name='Тақырыбы')
    content = models.TextField(verbose_name='Мазмұны')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes', verbose_name='Авторы')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Жазба'
        verbose_name_plural = 'Жазбалар'

    def __str__(self):
        return self.title
