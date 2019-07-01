# Generated by Django 2.2.1 on 2019-06-30 16:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorerapp', '0004_auto_20190629_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='place',
            name='creation_date',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
    ]
