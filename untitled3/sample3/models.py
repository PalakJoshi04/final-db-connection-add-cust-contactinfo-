from django.db import models
from .validators import *


class ContactInfo(models.Model):
    mobileNumber = models.PositiveIntegerField()
    phoneNumber = models.PositiveIntegerField()
    emailID = models.EmailField(max_length=50)


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True, validators=[validate_city])
    state = models.CharField(max_length=20, blank=True, null=True, validators=[validate_state])
    landmark = models.CharField(max_length=20, blank=True, null=True, validators=[validate_landmark])
    pincode = models.IntegerField(blank=True, null=True)


class Customer(ContactInfo, Address):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, validators=[validate_first_name])
    last_name = models.CharField(max_length=20, validators=[validate_last_name])
