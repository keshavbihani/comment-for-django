from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import ContactForm,LoginForm,RegisterForm

def home_page(request):
	context= {
		 "title":"friends with interest",
        "content":" Welcome to the homepage.",
	}

	return render(request, "home_page.html", context)


def contactform(request):
	form=ContactForm(request.POST or None)
	context={
		"title":"Contact :",
		"content":"For any query Contact at",
		"form":form
	}	
	return render(request, "contact/contact_form.html", context)

def loginform(request):
	form=LoginForm(request.POST or None)
	context={
		"title":"Contact :",
		"content":"For any query Contact at",
		"form":form
	}	
	return render(request, "auth/login.html", context)

def registerform(request):
	form=RegisterForm(request.POST or None)
	context={
		"title":"Contact :",
		"content":"For any query Contact at",
		"form":form
	}	
	return render(request, "auth/register.html", context)	