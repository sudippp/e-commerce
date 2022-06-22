from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]


class CustomerForm(forms.ModelForm):
    name = forms.CharField(label='Name',help_text="required*",error_messages={"required":"Enter Your Full Name"})
    locality = forms.CharField(label='Locality',help_text="required*",error_messages={"required":"Enter Your Locality"})
    city = forms.CharField(label='City',help_text="required*",error_messages={"required":"Enter Your City"})
    pincode = forms.IntegerField(label='Pincode',help_text="required*",error_messages={"required":"Enter Your Pincode"})
    mobile_number = forms.IntegerField(help_text="required*",label="Mobile Number", error_messages={"required":"Enter Your Mobile Number"})
    class Meta:
        model = Customer
        fields = ["name","locality","city","pincode","mobile_number"]
    
    def clean_name(self):
        name = str(self.cleaned_data.get("name"))
        if len(name) <= 10 :
            raise forms.ValidationError("Full Name should be 5 Chareter long !!")
        else:
            return name

    def clean_pincode(self):
        pincode = str(self.cleaned_data.get("pincode"))
        if len(pincode) != 6 :
            raise forms.ValidationError("Enter Valid Pincode !!")
        else:
            return pincode

    def clean_mobile_number(self):
        mobile_number = str(self.cleaned_data.get("mobile_number"))
        if len(mobile_number) != 10 :
            raise forms.ValidationError("Enter Valid Mobile Number !!")
        else:
            return mobile_number