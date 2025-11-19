from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('file', models.FileField(upload_to='docs/', verbose_name='Файл')),
                ('access', models.CharField(choices=[('public', 'Публичный'), ('client', 'Клиенты'), ('internal', 'Внутренний')], default='public', max_length=20, verbose_name='Доступ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
            ],
        ),
    ]
