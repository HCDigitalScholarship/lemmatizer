from django.shortcuts import render
from django.http import HttpResponse

def lemmatizer(request):
	return render(request,'lemmatizer.html')
 
# Create your views here.
