from django import forms
from django.forms import ModelForm
from .models import *

class RegisterForm(forms.ModelForm):
	date= forms.DateField(widget= forms.SelectDateWidget)
	time= forms.TimeField()


	class Meta:
		model = Register
		fields = '__all__'

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'



