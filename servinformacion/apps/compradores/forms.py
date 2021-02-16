from django import forms
from .models import *


class BuyerForm(forms.ModelForm):
    class Meta:
        model = compradores
        fields = "__all__"
