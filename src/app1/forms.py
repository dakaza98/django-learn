from django import forms
from phonenumbers import parse, is_valid_number
from django.utils.translation import ugettext_lazy as _


class PhoneField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super(PhoneField, self).__init__(*args, **kwargs)

    def clean(self, phonenumber):
        try:
            parsed_phone = parse(phonenumber, "SE")
            if not is_valid_number(parsed_phone):
                raise forms.ValidationError(_("Not a valid phonenumber"))

            return phonenumber
        except Exception:
            raise forms.ValidationError(_("Invalid phonenumber"))


# TODO: Create own phonefield
class PhoneForm(forms.Form):
    phone_number = PhoneField(label='Telefonnummer', max_length=100)
