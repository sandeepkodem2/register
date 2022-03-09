from django.shortcuts import render
from django.http import HttpResponse
from .models import Register1
from .forms import Register1Form
from django.shortcuts import redirect
# Create your views here.

def home(request):
    if request.method=='POST':
        form=Register1Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('register:success')
    else:
        form=Register1Form()
        return render(request,'register/register.html',{'form':form})



def success(request):
    return render(request,'register/success.html')