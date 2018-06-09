from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import reverse, render
from stock.forms import DepartmentForm, CategoryForm
from core.models import Contact, Address, Department, Category


def department_submit(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            address = Address.objects.create(country=data['country'], province=data['province'], city=data['city'],
                                             street=data['street'], number=data['number'],
                                             postal_code=data['postal_code'])
            contact = Contact.objects.create(name=data['contact_name'], email=data['email'],
                                             telephone=data['telephone'], telephone2=data['telephone_2'])
            Department.objects.create(name=data['department_name'], address=address, contact=contact)
            return HttpResponseRedirect(reverse('stock:index'))
    else:
        form = DepartmentForm()

    return render(request, 'stock/forms/department.html', {'form': form})


def category_submit(request, department_id):
    department = Department.objects.get(id=department_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Category.objects.create(name=data['name'], department=department)
            return HttpResponseRedirect(reverse('stock:categories', args=(department.id,)))
    else:
        form = CategoryForm()

    return render(request, 'stock/forms/category.html', {'form': form, 'department': department})
