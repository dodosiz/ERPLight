from django.shortcuts import render, get_list_or_404
from stock.models import *
from core.models import *


def index(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'stock/index.html', context=context)


def categories(request, department_id):
    department_categories = Category.objects.filter(department__id=department_id)
    context = {'categories': department_categories, 'department_id': department_id}
    return render(request, 'stock/categories.html', context=context)


def stock(request, category_id):
    stocks = get_list_or_404(Stock, product__category__id=category_id)
    context = {'stocks': stocks}
    return render(request, 'stock/stock.html', context)
