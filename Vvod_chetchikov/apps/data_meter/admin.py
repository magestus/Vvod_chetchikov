from django.contrib import admin
from .models import Data_meter


# Register your models here.


@admin.register(Data_meter)
class AdminData_meter(admin.ModelAdmin):
    pass
