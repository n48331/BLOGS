# Generated by Django 4.2.5 on 2023-12-04 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='location_city',
        ),
        migrations.RemoveField(
            model_name='post',
            name='type',
        ),
    ]
