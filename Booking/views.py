from django.shortcuts import render,redirect
from .forms import RegisterForm,ContactForm
from .models import Breakfast,Lunch,Dinner,Contact
from django.contrib import messages
from email.message import EmailMessage
from django.views.generic import View
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def index(req):
	review=Contact.objects.all()

	if req.method=="POST":
		email=req.POST.get('email')
		subject='Newletter Meal'
		msg='Thanks for subscribing to our Newsletter'
		rep_list=[email]

		send_mail(subject,msg,settings.EMAIL_HOST_USER,rep_list)
		return HttpResponse('Mail Sended')
	return render(req,'Booking/index.html',context={'review':review})


def register(request):
	context={}
	form =RegisterForm(request.POST or None) 
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Registered')
		return redirect('/')

	context['form']=form
	return render(request, "Booking/registertable.html", context) 



def contact(request):
	context={}
	form =ContactForm(request.POST or None) 
	if form.is_valid():
		form.save()
		messages.success(request, 'Successfully Submitted')
		return redirect('contact')

	context['form']=form
	return render(request, "Booking/contact.html", context) 


def menu(request):
	data3=Dinner.objects.all()

	

	data2=Lunch.objects.all()

	
	data1=Breakfast.objects.all()

	

	return render(request,"Booking/menu.html",context={'morning':data1,'lunch':data2,'dinner':data3}) 
	

