from django.shortcuts import render, redirect, get_object_or_404
from .forms import KnifeForm
from .models import Knife, Care, Repair
from .forms import OrderForm
def home(request):
    return render(request, 'home.html', {'title': 'Home Page'})

def info(request):
    return render(request, 'info.html', {'title': 'Info Page'})

def types(request):
    knives = Knife.objects.all()
    repairs = Repair.objects.all()
    cares = Care.objects.all()

    return render(request, 'types.html', {
        'title': 'Types Page',
        'knives': knives,
        'repairs': repairs,
        'cares': cares,
    })
def knife_detail(request, id):
    knife = Knife.objects.get(id=id)
    return render(request, 'knife_detail.html', {'knife': knife})

# Функція для ремонту
def repair_detail(request, id):
    repair = Repair.objects.get(id=id)
    return render(request, 'repair_detail.html', {'repair': repair})

# Функція для догляду
def care_detail(request, id):
    care = Care.objects.get(id=id)
    return render(request, 'care_detail.html', {'care': care})
def knives_view(request):
    knives = Knife.objects.all()
    return render(request, 'types.html', {'knives': knives})

def cares_view(request):
    cares = Care.objects.all()
    return render(request, 'care.html', {'cares': cares})

def repairs_view(request):
    repairs = Repair.objects.all()
    return render(request, 'repair.html', {'repairs': repairs})


def advice(request):
    return render(request, 'advice.html')


def create_knife(request):
    if request.method == 'POST':
        form = KnifeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = KnifeForm()
    return render(request, 'knife_form.html', {'form': form})

def make_order(request, category, product_id):
    category_map = {
        'knife': Knife,
        'repair': Repair,
        'care': Care,
    }

    if category not in category_map:
        return redirect('home')

    product_model = category_map[category]
    product = get_object_or_404(product_model, id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.category = category
            order.product_id = product.id
            order.product_name = product.name
            order.save()
            return render(request, 'order_success.html', {'order': order})
    else:
        form = OrderForm()

    return render(request, 'order_form.html', {'form': form, 'product': product, 'category': category})

