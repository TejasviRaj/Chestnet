from django.shortcuts import render


def upload(request):
    context = {}
    return render(request, 'api/index1.html', context)