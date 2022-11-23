# Generated by Django 4.1.3 on 2022-11-23 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_remove_categorymodeltranslation_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='catalog.categorymodel'),
            preserve_default=False,
        ),
    ]
