# Generated by Django 4.0 on 2021-12-15 15:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MembershipType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Adult', 'Adult'), ('Family', 'Family'), ('Student', 'Student')], help_text='Please select the type of membership', max_length=7, verbose_name='Member Type Name')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Membership Year')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
            options={
                'unique_together': {('name', 'year')},
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=5)),
                ('payment_type', models.CharField(choices=[('Cash', 'Cash'), ('Check', 'Check'), ('Paypal', 'Paypal')], max_length=6)),
                ('payment_date', models.DateField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='membership.membershiptype')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=24)),
                ('first_name', models.CharField(max_length=24)),
                ('address', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=24, null=True)),
                ('state', models.CharField(blank=True, max_length=24, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=14, null=True)),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='membership.membership')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='membership.user')),
            ],
        ),
    ]
