# Generated by Django 4.1.7 on 2023-03-23 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0004_alter_products_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='img',
            field=models.ImageField(max_length=500, null=True, upload_to=''),
        ),
    ]