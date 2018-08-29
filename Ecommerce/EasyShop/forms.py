from django import forms
from .models import Items,Users,Orders,Categories



class Users_Form(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name','address','mobile','email']
