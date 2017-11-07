from django.db import models

# Create your models here.



class Meter(models.Model):

    '''Администрирование счетчиков'''

    type_meter = models.CharField('Вид счетчика', max_length=45, null=True, blank=True)
    code_type_meter = models.CharField('Код счетчика', max_length=10, blank=True)
    #tariff = models.CharField('Тариф', max_length=15, null=True, blank=True)

    class Meta:
        verbose_name = 'Вид счетчика'
        verbose_name_plural = 'Виды счетчиков'

    def __str__(self):
        return str(self.type_meter) + '_' + str(self.code_type_meter)
