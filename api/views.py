from django.shortcuts import render
from django.http import HttpResponse
from .predictions import predict
import base64
import re


def upload(request):
    context = {}
    return render(request, 'api/index1.html', context)

def api(request):
    context = {}
    #return HttpResponse( '<img src = "blob:http://127.0.0.1:8000/a3e935de-231a-4b3a-821b-4bb33a656b60">')
    #return HttpResponse(request.GET.get("add", ""))
    a='<img src="'+ request.POST.get("add", "") + '">'
    return HttpResponse(a)

def first(request):
    context = {}
    return render(request, 'api/first.html', context)

def second(request):
    context = {}
    data= request.POST.get("val", "")
    print(len(data))
    # data += "=" * ((4 - len(data) % 4) % 4)
    imgdata = base64.b64decode(data+"===")
    #print(imgdata)
    d1=data[:len(data)]
    d2=data[len(data):]
    with open("d1.txt", 'w') as f:
        f.write(d1)
    with open("d2.txt", 'w') as f:
        f.write(d2)
    return HttpResponse(data)

    #return render(request, 'api/second.html', context)

def mult(request):
    f= request.FILES['file']

    print("hello")

    with open(request.FILES['file'].name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    data=predict(request.FILES['file'].name)
    print(data)
    print(request.FILES['file'].name)
    # data=['abc','cde']

    if(len(data)==1):
        data=data[0]
    else:
        data =', '.join(data[:-1]) + ' and ' + data[-1]
    return HttpResponse("Diagnosis Result:\r\n"+data)





