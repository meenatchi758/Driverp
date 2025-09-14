# forms.py
from django import forms
from .models import Bike

class BikeForm(forms.ModelForm):
    upload_image = forms.ImageField(required=False)

    class Meta:
        model = Bike
        exclude = ['image_data', 'image_type']

    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get('upload_image')

        if image_file:
            instance.image_data = image_file.read()
            instance.image_type = image_file.content_type

        if commit:
            instance.save()

        return instance
from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'reason', 'found_us', 'message']
        
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail Address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message'}),
            'reason': forms.Select(attrs={'class': 'form-select'}),  # Use Select widget for dropdown
            'found_us': forms.Select(attrs={'class': 'form-select'}), # Use Select widget for dropdown
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add placeholder prompt as first option in reason dropdown
        reason_choices = self.fields['reason'].choices
        self.fields['reason'].choices = [('', 'Reason to Contact')] + list(reason_choices)[1:]
        self.fields['reason'].required = True

        # Add placeholder prompt as first option in found_us dropdown
        found_us_choices = self.fields['found_us'].choices
        self.fields['found_us'].choices = [('', 'How did you find out about us ?')] + list(found_us_choices)[1:]
        self.fields['found_us'].required = True


