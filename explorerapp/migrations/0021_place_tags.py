# Generated by Django 2.2.1 on 2019-07-04 20:11

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('explorerapp', '0020_auto_20190701_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
