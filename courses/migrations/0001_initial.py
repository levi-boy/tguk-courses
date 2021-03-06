# Generated by Django 3.2.3 on 2021-05-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='news/', verbose_name='Фото')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(max_length=100, verbose_name='ФИО Родителя/Законного представителя')),
                ('parent_phone', models.CharField(max_length=100, verbose_name='Телефон Родителя/Законного представителя')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО ученика')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон ученика')),
                ('email', models.EmailField(max_length=254, verbose_name='Эл. почта')),
                ('school', models.CharField(max_length=100, verbose_name='Школа/класс')),
                ('address', models.CharField(max_length=250, verbose_name='Адресс проживания')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
