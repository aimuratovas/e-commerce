# Generated by Django 4.1.7 on 2023-03-22 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='cost',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
