from django.db import models


class News(models.Model):
    photo = models.ImageField('Фото', upload_to='news/')
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Record(models.Model):
    parent_name = models.CharField('ФИО Родителя/Законного представителя', max_length=100)
    parent_phone = models.CharField('Телефон Родителя/Законного представителя', max_length=100)
    name = models.CharField('ФИО ученика', max_length=100)
    phone = models.CharField('Телефон ученика', max_length=100)
    email = models.EmailField('Эл. почта')
    school = models.CharField('Школа/класс', max_length=100)
    address = models.CharField('Адресс проживания', max_length=250)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
