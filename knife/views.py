from django.shortcuts import render, redirect
from .forms import KnifeForm
from .models import Knife

def home(request):
    return render(request, 'home.html', {'title': 'Home Page'})

def info(request):
    return render(request, 'info.html', {'title': 'Info Page'})

def types(request):
    knives = Knife.objects.all()
    return render(request, 'knife/types.html', {'title': 'Types Page', 'knives': knives})


def advice(request):
    return render(request, 'advice.html')

def knife_list(request):
    knives = Knife.objects.all()
    return render(request, 'knife/types.html', {'knives': knives})

def create_knife(request):
    if request.method == 'POST':
        form = KnifeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = KnifeForm()
    return render(request, 'knife_form.html', {'form': form})
