from django.shortcuts import render
from django.db.models import Sum
from myapp5.models import Product

''' первое представлиние считаем сумму через базу данных'''


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


''' вторе представлиние считаем сумму через представление Pruduxts'''


def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


''' третье представлиние считаем сумму через шаблон'''


def total_in_template(request):
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 'myapp6/total_count.html', context)

'''Чтобы научить модель считаь в апп5 добавляем 3 строчки кода'''
