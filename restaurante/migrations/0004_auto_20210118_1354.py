# Generated by Django 3.1.5 on 2021-01-18 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0003_auto_20210118_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemorden',
            name='empaque',
        ),
        migrations.RemoveField(
            model_name='itemorden',
            name='observaciones',
        ),
        migrations.AddField(
            model_name='orden',
            name='empaque',
            field=models.CharField(choices=[('IN', 'Consumir en el sitio'), ('OU', 'Para llevar')], default='IN', max_length=2),
        ),
        migrations.AddField(
            model_name='orden',
            name='observaciones',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='valor',
            field=models.FloatField(blank=True, null=True),
        ),
    ]