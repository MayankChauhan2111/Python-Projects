# Generated by Django 3.1.1 on 2020-11-19 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_bid_producturl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='producturl',
        ),
    ]
