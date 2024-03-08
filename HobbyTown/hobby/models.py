from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Game(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя настольной игры')
    image = models.ImageField(upload_to='static/media/%Y/%m/%d/', verbose_name='Картинка настолки')
    desc = models.TextField(verbose_name='Описание игры')
    players_min = models.PositiveIntegerField(verbose_name='Минимальное количество игроков на игру')
    players_max = models.PositiveIntegerField(verbose_name='Максимальное количество игроков на игру')

    class Meta:
        verbose_name = 'Настолка'
        verbose_name_plural = 'Настолки'

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название события')
    image = models.ImageField(upload_to='static/media/%Y/%m/%d/', verbose_name='Картинка события')
    description = models.TextField(verbose_name='Описание события')
    places = models.PositiveIntegerField(verbose_name='Количество мест')
    date_start = models.DateTimeField(verbose_name='Дата начала')
    date_end = models.DateTimeField(verbose_name='Дата конца')
    price = models.PositiveIntegerField(verbose_name='Цена')
    address = models.CharField(max_length=255, verbose_name='Место провождения')

    class Meta:
        verbose_name = 'Игротека'
        verbose_name_plural = 'Игротеки'

    def __str__(self):
        return self.title


class EventGame(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Игротека')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Настолка')
    players = models.PositiveIntegerField(verbose_name='Количество человек')
    current = models.PositiveIntegerField(verbose_name='Количество записей', default=0)

    class Meta:
        verbose_name = 'Игра на игротеку'
        verbose_name_plural = 'Игры на игротеки'

    def __str__(self):
        return f'{self.event} to {self.game}'


class Sign(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя записи')
    number = PhoneNumberField(region='KZ', verbose_name='Номер записи')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Игрокета')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name} to {self.event}'


class SpecialSign(Sign):
    game = models.ForeignKey(EventGame, on_delete=models.CASCADE, verbose_name='Игра на игротеке')

    class Meta:
        verbose_name = 'Запись на игротеку + игру'
        verbose_name_plural = 'Записи на игротеки + игры'


class RegularSign(Sign):
    pass

    class Meta:
        verbose_name = 'Запись на игротеку'
        verbose_name_plural = 'Записи на игротеки'
