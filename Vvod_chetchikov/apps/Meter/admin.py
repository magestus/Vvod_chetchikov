from django.contrib import admin
from .models import Meter

# Register your models here.

@admin.register(Meter)
class AdminMeter(admin.ModelAdmin):
    pass