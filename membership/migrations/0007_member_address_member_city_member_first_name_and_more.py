# Generated by Django 4.0 on 2021-12-15 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0006_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='city',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='first_name',
            field=models.CharField(default='john', max_length=24),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='last_name',
            field=models.CharField(default='doe', max_length=24),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='postal_code',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='state',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
