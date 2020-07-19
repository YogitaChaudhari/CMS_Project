from django import forms
from myapp.models import User,Complaint

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

class ComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields='__all__'




