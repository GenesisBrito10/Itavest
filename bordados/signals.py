from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Bordado

@receiver(post_save, sender=get_user_model())
def assign_bordado_permissions(sender, instance, created, **kwargs):
    if created:
        
        instance.is_staff  = True

       
        content_type = ContentType.objects.get_for_model(Bordado)
        permissions = Permission.objects.filter(content_type=content_type)

      
        """ permissions = [
            Permission.objects.get(codename='add_bordado', content_type=content_type),
            Permission.objects.get(codename='change_bordado', content_type=content_type),
            Permission.objects.get(codename='delete_bordado', content_type=content_type),
            Permission.objects.get(codename='view_bordado', content_type=content_type),
            # Adicione mais permissões conforme necessário
        ] """

        
        instance.user_permissions.set(permissions)

        instance.save()
