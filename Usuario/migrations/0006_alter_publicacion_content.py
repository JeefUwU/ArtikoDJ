# Generated by Django 4.1.2 on 2023-07-06 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0005_rename_post_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='content',
            field=models.ImageField(upload_to=''),
        ),
    ]
