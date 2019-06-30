from django.shortcuts import render
from django.http import HttpResponse


def upload(request):
    context = {}
    return render(request, 'api/index1.html', context)

def api(request):
    context = {}
    #return HttpResponse( '<img src = "blob:http://127.0.0.1:8000/a3e935de-231a-4b3a-821b-4bb33a656b60">')
    #return HttpResponse(request.GET.get("add", ""))
    a='<img src="'+ request.GET.get("add", "") + '">'
    return HttpResponse(a)

