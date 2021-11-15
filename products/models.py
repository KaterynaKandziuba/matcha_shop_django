from django.db import models
# https://metanit.com/python/django/    Руководство по веб-фреймворку Django

class Product(models.Model):
    # свойства моделей. Каждое св-во - это столбец в соотв таблице
    title = models.CharField(max_length=100)  # https://metanit.com/python/django/4.2.php
    about = models.TextField(max_length=500) # Типы полей формы
    picture = models.FileField(upload_to='pictures/')
    price = models.FloatField()
    amount = models.IntegerField()

    def __str__(self) -> str:
        return str(self.title)