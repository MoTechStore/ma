# Generated by Django 3.2.3 on 2021-08-10 09:25

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=1000)),
                ('file_number', models.CharField(max_length=1000)),
                ('cupboard_name', models.CharField(max_length=1000)),
                ('cupboard_number', models.CharField(max_length=1000)),
                ('shelve_number', models.CharField(max_length=1000)),
                ('about_file', models.CharField(max_length=1000)),
                ('current_owner', models.CharField(blank=True, max_length=1000, null=True)),
                ('ref_number', models.CharField(max_length=1000)),
                ('keyword', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
                ('receiver', models.CharField(max_length=1000)),
                ('contact', models.CharField(max_length=1000)),
                ('desc', models.CharField(max_length=1000)),
                ('ref_number', models.CharField(max_length=1000, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Letters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=1000)),
                ('receiver_address', models.CharField(max_length=1000)),
                ('receiver_name', models.CharField(max_length=1000)),
                ('contact_two', models.CharField(max_length=1000)),
                ('desc_two', models.CharField(max_length=1000)),
                ('ref_number_two', models.CharField(max_length=1000, null=True)),
                ('date_two', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=1000)),
                ('document_number', models.CharField(max_length=1000)),
                ('file_name', models.CharField(max_length=1000)),
                ('file_number', models.CharField(max_length=1000)),
                ('cupboard_name', models.CharField(max_length=1000)),
                ('cupboard_number', models.CharField(max_length=1000)),
                ('shelve_number', models.CharField(max_length=1000)),
                ('about_document', models.CharField(max_length=1000)),
                ('current_owner', models.CharField(blank=True, max_length=1000, null=True)),
                ('ref_number', models.CharField(max_length=1000)),
                ('name_list', models.CharField(max_length=1000)),
                ('accessed_no', models.IntegerField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_cis_officer', models.BooleanField(default=False)),
                ('is_rms_officer', models.BooleanField(default=False)),
                ('is_cis_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
