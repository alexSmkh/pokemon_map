from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField('название на русском', max_length=200)
    title_en = models.CharField('название на английском', max_length=200)
    title_jp = models.CharField('название на японском', max_length=200)
    image = models.ImageField('картинка покемона')
    description = models.TextField('описание')
    next_evolution = models.ForeignKey(
        'Pokemon',
        related_name='next_life_stage',
        verbose_name='следующая стадия развития покемона',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    previous_evolution = models.ForeignKey(
        'Pokemon',
        related_name='previous_life_stage',
        verbose_name='предыдущая стадия развития покемона',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'{self.title_ru}'


class PokemonEntity(models.Model):
    latitude = models.FloatField('широта')
    longitude = models.FloatField('долгота')
    appeared_at = models.DateTimeField('дата и время появления на карте')
    disappeared_at = models.DateTimeField('дата и время удаления с карты')
    level = models.IntegerField('уровень', null=True, blank=True)
    health = models.IntegerField('здоровье', null=True, blank=True)
    strength = models.IntegerField('сила', null=True, blank=True)
    defence = models.IntegerField('защита', null=True, blank=True)
    stamina = models.IntegerField('выносливость', null=True, blank=True)
    pokemon = models.ForeignKey(Pokemon, verbose_name='покемон', on_delete=models.CASCADE)
