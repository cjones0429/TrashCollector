from django.urls import path

from . import views


# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns


app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('account_info_details/', views.account_info_details, name="account_info_details"),
    path('pickup_day/', views.pickup_day, name="pickup_day"),
    path('one_time_pickup/', views.one_time_pickup, name="one_time_pickup"),
    path('suspend_pickup/', views.suspend_pickup, name="suspend_pickup"),
    path('edit/', views.edit, name="edit")
]
