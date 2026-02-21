from datetime import date

from django import forms

from cars.models import Car
from rentals.models import Rental


class RentalForm(forms.ModelForm):
    car = forms.ModelChoiceField(
        queryset=Car.objects.all(),
        empty_label='Select a car',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Rental
        fields = ['car', 'customer_name', 'customer_email', 'start_date', 'end_date']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        car = self.cleaned_data['car']
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')
        if start and end:
            if end < start:
                raise forms.ValidationError('End date must be before start date')
            if start < date.today():
                raise forms.ValidationError('Start date cannot be in the past')
            conflict = Rental.objects.filter(
                car=car,
                end_date__gte=start,
                start_date__lte=end
            ).exists()
            if conflict:
                raise forms.ValidationError(f'This car is already rented from {start} to {end}')
