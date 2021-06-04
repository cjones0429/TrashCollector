from django.db import models
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50, default=("temp"))
    pickup_day = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=50, null=True)
    account_balance = models.IntegerField(default=0)
    one_time_pickup = models.DateField(null=True)
    suspension_start = models.DateField(null=True)
    suspension_end = models.DateField(null=True)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
