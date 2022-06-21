from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class MyUserCreationForm(UserCreationForm):
    mobile_number = forms.IntegerField(help_text="required*",label="Mobile Number", error_messages={"required":"Enter Your Mobile Number"})
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2","mobile_number"]

    def clean_mobile_number(self):
        mobile_number = str(self.cleaned_data.get("mobile_number"))
        if len(mobile_number) != 10 :
            raise forms.ValidationError("Enter Valid Mobile Number !!")
        else:
            return mobile_number

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name","locality","city","pincode","mobile_number"]