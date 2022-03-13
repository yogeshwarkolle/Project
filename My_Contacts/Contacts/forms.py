from django import forms


from .models import Credentials, Data


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Credentials
        fields = [
            "email",
            "password",
            "scode"
        ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = [
            "name",
            "phn",
            "email"
        ]
