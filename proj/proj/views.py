from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    

    m1=request.POST.get("fname")
    m2=request.POST.get("lname")
    data={
        'a':m1,
        'b':m2

    }

    
    return render(request,"index.html",data)