from django import forms
from .models import Password

class PasswordForm(forms.ModelForm):
    def clean_phone(self):
        cleaned_data=self.cleaned_data['phone']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字!')
        return int(cleaned_data)
    class Meta:
        model=Password
        fields=(
            'appname','user','email','phone','password','image1'
        )