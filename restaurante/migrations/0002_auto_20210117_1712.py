# Generated by Django 3.1.5 on 2021-01-17 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='restaurante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurante.restaurante'),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='logo',
            field=models.ImageField(blank=True, default='logos_restaurantes/mazda.jpg', null=True, upload_to='logos_restaurantes/'),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
