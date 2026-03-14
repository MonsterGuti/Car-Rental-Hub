from django import forms
from cars.models import Car, Brand


class CarFilterForm(forms.Form):
    brand = forms.CharField(
        required=False,
        label='Brand',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Filter by brand'})
    )
    sort = forms.ChoiceField(
        required=False,
        choices=[('price', 'Price'), ('year', 'Newest')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'brand': forms.Select(attrs={'class': 'form-select'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Car Model'}),
            'car_type': forms.Select(attrs={'class': 'form-select'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year'}),
            'price_per_day': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price per day'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'features': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'brand': 'Brand',
            'model': 'Model',
            'year': 'Year of Manufacture',
            'price_per_day': 'Price per Day',
            'image': 'Upload image',
            'is_available': 'Available',
            'features': 'Features',
        }
        help_texts = {
            'features': 'Select all features that apply',
            'is_available': 'Check if the car is currently available for rent',
        }

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year and (year < 1980 or year > 2026):
            raise forms.ValidationError("Year must be between 1980 and 2026")
        return year

    def clean_price_per_day(self):
        price = self.cleaned_data.get('price_per_day')
        if price and price <= 0:
            raise forms.ValidationError("Price per day must be positive")
        return price


class CarDeleteForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'brand': forms.Select(attrs={'class': 'form-select', 'disabled': True}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'disabled': True}),
            'price_per_day': forms.NumberInput(attrs={'class': 'form-control', 'disabled': True}),
            'image': forms.URLInput(attrs={'class': 'form-control', 'disabled': True}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input', 'disabled': True}),
            'features': forms.CheckboxSelectMultiple(attrs={'disabled': True}),
        }


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'country']

        labels = {
            'name': 'Brand Name',
            'country': 'Country of Origin',
        }

        help_texts = {
            'name': 'Enter the name of the car brand.',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. BMW',
                'class': 'form-control'
            }),
            'country': forms.TextInput(attrs={
                'placeholder': 'e.g. Germany',
                'class': 'form-control'
            }),
        }

        error_messages = {
            'name': {
                'unique': 'This brand already exists.',
                'required': 'Please enter a brand name.',
            },
            'country': {
                'required': 'Please enter the country of origin.',
            },
        }


from django import forms
from .models import Feature


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = '__all__'

        labels = {
            'name': 'Feature Name',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Navigation, Heated Seats'
            })
        }
