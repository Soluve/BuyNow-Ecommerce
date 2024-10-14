from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'

    
    def ready(self):
        from django.db.models.signals import post_save
        from django.contrib.auth.models import User
        
        post_save.connect(self.create_customer, sender=User)

    @staticmethod
    def create_customer(sender, instance, created, **kwargs):
        from .models import Customer
        if created:
            Customer.objects.create(user=instance)