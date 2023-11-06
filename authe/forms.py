from typing import Any
from django import forms
from authe.models import register_model
from django.contrib.auth.hashers import make_password


class register_form(forms.ModelForm):
    repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = register_model
        fields = ['username', 'first_name', 'last_name',
                  'email', 'phone', 'dob', 'gender', 'img', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password'] == self.cleaned_data['repassword']:
            user.password = make_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user
        else:
            raise ValueError("password and repasssword is incorrect")

