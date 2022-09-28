from cProfile import label
from dataclasses import fields
from pyexpat import model
from secrets import choice
from urllib import request
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Answer, Kadai,Users,KadaiAdmin,KadaiQuestion

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
       model = User
       fields = ("username", "password1", "password2",)

from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       #htmlの表示を変更可能にします
       self.fields['username'].widget.attrs['class'] = 'form-control'
       self.fields['password'].widget.attrs['class'] = 'form-control'

#class AnswerForm(forms.Form):
#    text = forms.CharField(widget=forms.Textarea(),label='') 

#class RadioForm(forms.Form):
    
    

#class CheckForm(forms.Form):
#    kadai = Kadai.objects.all()
#    Astr = 'ee\nff\ngg\nhh'
#    data = Astr
#    selectdata=[]
#    for item in data:
#        selectdata.append((item,item))
#
#    choice = forms.MultipleChoiceField(\
#        choices=selectdata,widget=forms.CheckboxSelectMultiple)

