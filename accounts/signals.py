from .models import Customer 
from django.contrib.auth.models import User,Group 
from django.db.models.signals import post_save

def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user = instance,
            name = instance.username,
        )
        print('Profile cretead')
post_save.connect(customer_profile, sender=User)