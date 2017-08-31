from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'mobileNumber', 'phoneNumber', 'emailID', 'address1', 'address2', 'city', 'state', 'landmark', 'pincode']
