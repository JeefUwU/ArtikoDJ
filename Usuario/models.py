from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagenU = models.ImageField()

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Publicacion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.ImageField()

    class Meta:
        ordering =['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'

class etiqueta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return(self.nombre)

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=450)
    etiqueta = models.ForeignKey(etiqueta, on_delete=models.PROTECT)
    imagen = models.FileField(upload_to="productos", null=True)

    def __str__(self):
        return(self.nombre)


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagenU = models.ImageField(default= 'a.png')

    def __str__(self):
        return f'Perfil de {self.user.username}'

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
