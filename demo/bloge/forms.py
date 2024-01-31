from django import forms
from django.core import validators

class TecharsRegistraton(forms.Form):
    first_name = forms.CharField(label='Enter your first name')
    last_name = forms.CharField()
    email = forms.EmailField(initial='shawonshakib@gmail.com', disabled=True)
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput)
    checkbox = forms.CharField(widget=forms.CheckboxInput)

    def clean(self):
        cleaned_data = super().clean()
        rightpass = self.cleaned_data['password']
        wrongpass = self.cleaned_data['repassword']
        if wrongpass != rightpass:
            raise forms.ValidationError('password does not match')