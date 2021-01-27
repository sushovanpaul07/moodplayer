# from django import forms
#
#
# class DocumentForm(forms.Form):
#     docfile = forms.FileField(
#         label='Select a file',
#     )
# forms.py
from django import forms
from .models import *


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']
