from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        """ class for the modelForm """
        model = Item
        fields = [ 'name', 'done_status']
