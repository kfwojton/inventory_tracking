from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# from multiselectfield import MultiSelectField


class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    organization = models.CharField(verbose_name="Name",max_length=100, blank=False,)
    location_city = models.CharField(verbose_name="City",max_length=100, blank=True,)
    # location_state = models.CharField(verbose_name="State",choices=state_validation_choices,max_length=2, blank=True,)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)


class Inventory(models.Model):
    name = models.CharField(verbose_name="title",max_length=100, blank=False,)
    type_of_inventory = models.CharField(max_length=100, blank=False,)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    # need to handle this on in the POST function block
    created_by = models.ForeignKey(User,default=None,on_delete=models.CASCADE,blank=True, null=True)

class Client(models.Model):
    company_name = models.CharField(verbose_name="title",max_length=100, blank=False,)

class Invoice(models.Model):
    company = models.ForeignKey(Client, default=None,on_delete=models.CASCADE,blank=True)
    cost_of_invoice = models.DecimalField(max_digits=50, decimal_places=2)
    date_billed = models.DateTimeField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
