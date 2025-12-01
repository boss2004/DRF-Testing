from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    # username = None

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название тега')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Теги для постов')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title
    

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(verbose_name='Контент')

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='posts',
        null=True,
        blank=True,
        verbose_name='Категория'
    )
    
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Теги')
    published = models.BooleanField(default=False, verbose_name='Опубликован')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title