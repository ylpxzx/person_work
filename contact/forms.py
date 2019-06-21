from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model=Contact
        fields=(
            'name','word','relation','phone','email','sex'
        )