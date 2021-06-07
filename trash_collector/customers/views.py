from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
from django.urls import reverse
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user
    # It will be necessary while creating a customer/employee to assign the logged-in user as the user foreign key
    # This will allow you to later query the database using the logged-in user,
    # thereby finding the customer/employee profile that matches with the logged-in user.
    print(user)
    return render(request, 'customers/index.html')


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        pickup_day = request.POST.get('pickup_day')
        zip_code = request.POST.get('zip_code')
        one_time_pickup = request.POST.get('one_time_pickup')
        new_customer = Customer(name=name,
                                address=address,
                                zip_code=zip_code,
                                pickup_day=pickup_day,
                                one_time_pickup=one_time_pickup,
                                user=request.user)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:details'))
    else:
        return render(request, 'customers/create.html')


def edit(request):
    customer = Customer.objects.get(user=request.user)
    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.address = request.POST.get('address')
        customer.zip_code = request.POST.get('zip_code')
        customer.pickup_day = request.POST.get('pickup_day')
        customer.one_time_pickup = request.POST.get('one_time_pickup')
        customer.save()
        return HttpResponseRedirect(reverse('customer:index'))
    else:
        context = {
            'customer': customer
        }
        return render(request, 'customer/edit.html', context)


def delete(request):
    customer = Customer.objects.get(user=request.user)
    customer.delete()
    customer = customer.objects.all()
    context = {
        'customer': customer
    }
    return render(request, 'customer/index.html', context)


def pickup_day(request):
    customer = Customer.objects.get(user=request.user)
    if request.method == 'POST':
        customer.one_time_pickup = request.POST.get('one_time_pickup')
        customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/pickup_day')


def one_time_pickup(request):
    customer = Customer.objects.get(user=request.user)
    if request.method == 'POST':
        customer.one_time_pickup = request.Post.get('One-Time Pickup')
        customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/one_time_pickup')


def account_info_details(request):
    try:
        customer = Customer.objects.get(user=request.user)
        context = {
            'customer': customer
        }
        return render(request, 'customer/account_info_details.html', context)
    except:
        create(request)


def suspend_pickup(request):
    customer = Customer.objects.get(user=request.user)
    if request.method == 'POST':
        customer.suspension_start = request.Post.get('suspend_start')
        customer.suspension_end = request.Post.get('suspend_end')
        customer.save()
    else:
        return render(request, 'customer/suspend_pickup.html')

