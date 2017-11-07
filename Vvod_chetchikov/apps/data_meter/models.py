from django.db import models
from datetime import *
from Vvod_chetchikov.apps.Meter.models import Meter
# Create your models here.


class Data_meter(models.Model):

    '''Ввод показаний счетчиков'''

    room_number = models.IntegerField('номер квартиры')
    type_meter = models.ForeignKey(Meter, verbose_name='Вид счётчика')
    accounting_year = models.IntegerField('Год учета', help_text='Введите год учёта', null=True)
    accounting_month = models.IntegerField('Месяц учета', help_text='Введите месяц учёта', null=True)
    dannie = models.IntegerField('Показание прибора', blank=False)
    date = models.DateTimeField('дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Данные счетчика'
        verbose_name_plural = 'Данные счетчиков'

    def __str__(self):
        return 'Данные счетчика {}'.format(self.id)

    class ChoiceField():
        pass

