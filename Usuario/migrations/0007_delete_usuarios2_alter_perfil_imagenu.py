# Generated by Django 4.1.2 on 2023-07-06 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0006_alter_publicacion_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuarios2',
        ),
        migrations.AlterField(
            model_name='perfil',
            name='imagenU',
            field=models.ImageField(default='a.png', upload_to=''),
        ),
    ]
