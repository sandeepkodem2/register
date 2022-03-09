from django import forms
from .models import Register1
from django.forms import ModelForm
from django import forms

GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female')
]


class Register1Form(ModelForm):
    Gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    class Meta:
        model=Register1
        fields=['Name','DOB','Email_id','Phone_Number','Gender','Flat_No','Street','Country','Upload_Photo']

        widgets = {
               'Name':forms.TextInput(attrs={'class':'form-control'}),
               'Email_id':forms.EmailInput(attrs={'class':'form-control'}),
               'DOB':forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
               'Phone_Number':forms.NumberInput(attrs={'class':'form-control'}),
               'Flat_No':forms.NumberInput(attrs={'class':'form-control'}),
               'Street':forms.TextInput(attrs={'class':'form-control'}),
               'Country':forms.Select(attrs={'class':'form-control'}),
               
               
       
        }
        
 
        
     