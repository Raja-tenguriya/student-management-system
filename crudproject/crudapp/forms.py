from django import forms 
from .models import student

class AddstudentForm(forms.ModelForm):   
    class Meta:
        model = student
        fields = ("roll","name","cls","city")

        labels = {
            'roll': 'R.No',
            'name': 'Name',
            'cls': 'class',
            'city': 'City',
        }

        widgets = {
            'roll' :forms.NumberInput(attrs={'class':'border border-gray-800 rounded-lg p-2 w-3/4 m-4 bg-gray-100'}),
            'name' :forms.TextInput(attrs={'class':'border border-gray-800 rounded-lg p-2 w-3/4 m-4 bg-gray-100'}),
            'cls' :forms.TextInput(attrs={'class':'border border-gray-800 rounded-lg p-2 w-3/4 m-4 bg-gray-100'}),
            'city' :forms.TextInput(attrs={'class':'border border-gray-800 rounded-lg p-2 w-3/4 m-4 bg-gray-100'}),
        }

