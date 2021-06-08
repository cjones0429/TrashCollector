from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('filter_customers_in_pickup_area/', views.filter_customers_in_pickup_area, name='filter_customers_in_pickup_area'),
    path('confirm_pickup/<int:customer_id/', views.confirm_pickup, name='confirm_pickup'),
    path('create/', views.create, name='create')
]