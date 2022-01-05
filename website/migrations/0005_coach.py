# Generated by Django 4.0 on 2022-01-05 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_sponsor_alter_boardmember_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=45)),
                ('first_name', models.CharField(max_length=45)),
                ('title', models.CharField(max_length=255)),
                ('biography', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]