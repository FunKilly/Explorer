# Generated by Django 2.2.1 on 2019-07-28 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planninghistory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='order',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='product',
            new_name='place',
        ),
    ]
