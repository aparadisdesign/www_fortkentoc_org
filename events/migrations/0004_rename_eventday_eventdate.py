# Generated by Django 4.0 on 2022-01-05 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_rename_date_eventday_event_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventDay',
            new_name='EventDate',
        ),
    ]