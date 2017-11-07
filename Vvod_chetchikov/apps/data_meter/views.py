from django.http import HttpResponse
from django.shortcuts import render
from Vvod_chetchikov.apps.data_meter.models import Data_meter
from Vvod_chetchikov.apps.Meter.models import Meter
from Vvod_chetchikov.apps.data_meter.forms import data_meterform


# Create your views here.

def index(request):
    meters = Meter.objects.all()

    form = data_meterform(initial={
        "type_meter": Meter.objects
        })

    context = {
        'meters': meters,
        'form': form
    }
    return render(request, 'index.html', context)

# def data__meter(self, index):
