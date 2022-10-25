"""Forms of the project."""
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widget = {'description' : forms.Textarea(), 'quantity' : forms.NumberInput()}
    # name = forms.CharField(label='name')
    # description = forms.CharField(label='description', widget=forms.Textarea())
    # quantity = forms.CharField(label='quantity', widget=forms.NumberInput())
# Create your forms here.
#testing push
