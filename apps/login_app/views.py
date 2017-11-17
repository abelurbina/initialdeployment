from future import unicode_literals
from .models import User
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect
  
def index(request):
	if "user" in session:
		return redirect('/success')
	else:
		return render(request, index.html)


