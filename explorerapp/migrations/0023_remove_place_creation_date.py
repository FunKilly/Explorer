# Generated by Django 2.2.1 on 2019-08-14 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorerapp', '0022_auto_20190728_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='creation_date',
        ),
    ]
