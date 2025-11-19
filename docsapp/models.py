from django.db import models

class Document(models.Model):
    ACCESS_CHOICES = [
        ('public', 'Публичный'),
        ('client', 'Клиенты'),
        ('internal', 'Внутренний'),
    ]

    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('Слаг', unique=True)
    description = models.TextField('Описание', blank=True)
    file = models.FileField('Файл', upload_to='docs/')
    access = models.CharField('Доступ', max_length=20, choices=ACCESS_CHOICES, default='public')
    created_at = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документация'

    def __str__(self):
        return self.title
