from django.apps import apps
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Employee

from django.urls import reverse


from django.urls import reverse

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db
    customers = apps.get_model('customers.Customer')
    user = request.user
    try:
        logged_in_employee = Employee.objects.get(user=user)
    except:
        return render(request, 'employees/create.html')
    employee_customers = customers(zip_code=logged_in_employee.zip_code)
    context = {
        'employee_customers': employee_customers,
        'logged_in_employee': logged_in_employee
    }
    return render(request, 'employees/index.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employee = Employee(name=name, zip_code=zip_code, user=request.user)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')


def confirm_pickups(request, customer_id):
    if request.method == 'GET':
        customers = apps.get_model('customers.Customer')
        customer = customers.objects.get(id=customer_id)
        customer.account_balance += 15
        customer.confirm_pickup = True
        customer.save()
        return render(request, 'employees/confirm.html')
    else:
        return render(request, 'employees/customers_today.html')


def filter_pickups(request):
    pass
