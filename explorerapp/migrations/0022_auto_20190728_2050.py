# Generated by Django 2.2.1 on 2019-07-28 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorerapp', '0021_place_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='location_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
