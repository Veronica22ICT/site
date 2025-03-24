from django.shortcuts import render


def home(request):
    context = {'title': 'Home Page'}
    return render(request, 'home.html',context)
def info(request):
    context = {'title': 'Info Page'}
    return render(request, 'info.html',context)
def types(request):
    context = {'title': 'Types Page'}
    return render(request, 'types.html',context)
def links(request):
    context = {'title': 'Links Page'}
    return render(request, 'links.html',context)
def advice(request):
    return render(request, 'advice.html')