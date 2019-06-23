from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from first_app.models import Topic,Webpage,AccessRecord
# Create your views here.

def index(request):
  
    
    return render(request,'first_app/index.html',context=date_dict)



