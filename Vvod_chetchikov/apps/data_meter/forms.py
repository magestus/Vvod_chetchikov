from django import forms
from Vvod_chetchikov.apps.data_meter.models import Data_meter
from Vvod_chetchikov.apps.Meter.models import Meter

class data_meterform(forms.ModelForm):
    #type_meter = forms.ModelChoiceField(queryset=Meter.objects.all)
    class Meta:
        model = Data_meter
        fields = ['room_number', 'accounting_month', 'accounting_year', 'type_meter', 'dannie']