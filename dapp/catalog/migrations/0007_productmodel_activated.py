# Generated by Django 4.1.3 on 2022-11-23 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_productmodel_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='activated',
            field=models.BooleanField(default=False, verbose_name='Активирован'),
        ),
    ]