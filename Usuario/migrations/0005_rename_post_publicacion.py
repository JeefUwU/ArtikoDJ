# Generated by Django 4.1.2 on 2023-07-05 23:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Usuario', '0004_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Publicacion',
        ),
    ]