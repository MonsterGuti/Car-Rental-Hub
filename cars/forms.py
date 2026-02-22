from django import forms
from cars.models import Car


class CarFilterForm(forms.Form):
    brand = forms.CharField(
        required=False,
        label='Brand',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Filter by brand'})
    )
    sort = forms.ChoiceField(
        required=False,
        choices=[('price', 'Price'), ('year', 'Newest')],
        widget=forms.Select(attrs={'class':'form-select'})
    )


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'price_per_day', 'image', 'is_available', 'features']
        widgets = {
            'brand': forms.Select(attrs={'class':'form-select'}),
            'model': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Car Model'}),
            'year': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Year'}),
            'price_per_day': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Price per day'}),
            'image': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Image URL'}),
            'is_available': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'features': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'brand': 'Brand',
            'model': 'Model',
            'year': 'Year of Manufacture',
            'price_per_day': 'Price per Day',
            'image': 'Image URL',
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
            'brand': forms.Select(attrs={'class':'form-select', 'disabled': True}),
            'model': forms.TextInput(attrs={'class':'form-control', 'disabled': True}),
            'year': forms.NumberInput(attrs={'class':'form-control', 'disabled': True}),
            'price_per_day': forms.NumberInput(attrs={'class':'form-control', 'disabled': True}),
            'image': forms.URLInput(attrs={'class':'form-control', 'disabled': True}),
            'is_available': forms.CheckboxInput(attrs={'class':'form-check-input', 'disabled': True}),
            'features': forms.CheckboxSelectMultiple(attrs={'disabled': True}),
        }