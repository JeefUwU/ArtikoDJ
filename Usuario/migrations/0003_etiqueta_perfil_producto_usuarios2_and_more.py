# Generated by Django 4.1.2 on 2023-07-05 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Usuario', '0002_rename_alumno_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenU', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField(max_length=450)),
                ('imagen', models.FileField(null=True, upload_to='productos')),
                ('etiqueta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Usuario.etiqueta')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id_genero',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]