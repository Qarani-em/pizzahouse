# Generated by Django 4.1.7 on 2023-04-16 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_item_onoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='onOffer',
            field=models.BooleanField(default=False),
        ),
    ]