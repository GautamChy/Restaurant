# Generated by Django 5.2 on 2025-04-29 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0004_rename_category_food_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='field',
            field=models.CharField(default='abc', max_length=100),
        ),
    ]
