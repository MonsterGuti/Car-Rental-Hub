from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['car', 'customer_name', 'content', 'rating']
        widgets = {
            'car': forms.Select(attrs={'class': 'form-select'}), # Използваме Select за избор на кола
            'customer_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write your review here', 'rows':3}),
            'rating': forms.NumberInput(attrs={'class':'form-control', 'min':1, 'max':5}),
        }
        labels = {
            'car': 'Select Car',
            'customer_name': 'Name',
            'content': 'Review',
            'rating': 'Rating (1-5)',
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating and (rating < 1 or rating > 5):
            raise forms.ValidationError("Rating must be between 1 and 5")
        return rating