# Generated by Django 4.0 on 2022-01-05 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_event_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='cost',
        ),
    ]
