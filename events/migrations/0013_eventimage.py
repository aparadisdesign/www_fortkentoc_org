# Generated by Django 4.0 on 2022-01-05 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_eventimagegallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/events/images/% Y/% m/% d/')),
                ('caption', models.CharField(max_length=255)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.eventimagegallery')),
            ],
        ),
    ]
