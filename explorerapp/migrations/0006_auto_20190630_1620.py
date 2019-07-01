# Generated by Django 2.2.1 on 2019-06-30 16:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('explorerapp', '0005_auto_20190630_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='rating',
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MaxValueValidator(5)])),
                ('num_of_ratings', models.IntegerField(default=0, editable=False)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explorerapp.Place')),
            ],
        ),
    ]
