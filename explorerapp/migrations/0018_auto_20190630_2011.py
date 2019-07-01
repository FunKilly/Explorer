# Generated by Django 2.2.1 on 2019-06-30 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorerapp', '0017_auto_20190630_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='rating',
        ),
        migrations.AddField(
            model_name='place',
            name='num_of_ratings',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='place',
            name='sum_of_rating',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=9),
        ),
    ]
