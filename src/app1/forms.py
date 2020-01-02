from django import forms


# TODO: Create own phonefield
class PhoneForm(forms.Form):
    phone_number = forms.CharField(label='Telefonnummer', max_length=100)
