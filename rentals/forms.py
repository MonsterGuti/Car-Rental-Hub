from datetime import date

from django import forms
from rentals.models import Rental


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['car', 'customer_name', 'customer_email', 'start_date', 'end_date']
        widgets = {
            'car': forms.TextInput(attrs={'class': 'form-select'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')
        if start and end:
            if end < start:
                raise forms.ValidationError('End date must be before start date')
            if start < date.today():
                raise forms.ValidationError('Start date cannot be in the past')
