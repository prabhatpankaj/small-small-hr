# Generated by Django 2.0.6 on 2018-06-16 15:33

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import private_storage.fields
import private_storage.storage.files


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('created',
                 models.DateTimeField(
                     auto_now_add=True, verbose_name='Created')),
                ('modified',
                 models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('start', models.DateTimeField(verbose_name='Start Date')),
                ('end', models.DateTimeField(verbose_name='End Date')),
                ('reason',
                 models.TextField(
                     blank=True, default='', verbose_name='Reason')),
                ('status',
                 models.CharField(
                     blank=True,
                     choices=[('1', 'Approved'), ('3', 'Pending'),
                              ('2', 'Rejected')],
                     default='3',
                     max_length=1,
                     verbose_name='Status')),
                ('comments',
                 models.TextField(
                     blank=True, default='', verbose_name='Comments')),
                ('leave_type',
                 models.CharField(
                     blank=True,
                     choices=[('1', 'Sick Leave'), ('2', 'Regular Leave')],
                     default='2',
                     max_length=1,
                     verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Leave',
                'verbose_name_plural': 'Leave',
                'ordering': ['staff', 'start'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OverTime',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('created',
                 models.DateTimeField(
                     auto_now_add=True, verbose_name='Created')),
                ('modified',
                 models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('reason',
                 models.TextField(
                     blank=True, default='', verbose_name='Reason')),
                ('status',
                 models.CharField(
                     blank=True,
                     choices=[('1', 'Approved'), ('3', 'Pending'),
                              ('2', 'Rejected')],
                     default='3',
                     max_length=1,
                     verbose_name='Status')),
                ('comments',
                 models.TextField(
                     blank=True, default='', verbose_name='Comments')),
                ('date', models.DateField(verbose_name='Date')),
                ('start', models.TimeField(verbose_name='Start')),
                ('end', models.TimeField(verbose_name='End')),
            ],
            options={
                'verbose_name': 'Overtime',
                'verbose_name_plural': 'Overtime',
                'ordering': ['staff', 'date', 'start'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('created',
                 models.DateTimeField(
                     auto_now_add=True, verbose_name='Created')),
                ('modified',
                 models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('name', models.CharField(max_length=255,
                                          verbose_name='Name')),
                ('description',
                 models.TextField(
                     blank=True, default='', verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
                'ordering': ['name', 'created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaffDocument',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('created',
                 models.DateTimeField(
                     auto_now_add=True, verbose_name='Created')),
                ('modified',
                 models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('name', models.CharField(max_length=255,
                                          verbose_name='Name')),
                ('description',
                 models.TextField(
                     blank=True, default='', verbose_name='Description')),
                ('file',
                 private_storage.fields.PrivateFileField(
                     help_text='Upload staff member drocument',
                     storage=private_storage.storage.files.
                     PrivateFileSystemStorage(),
                     upload_to='staff-documents/',
                     verbose_name='File')),
            ],
            options={
                'verbose_name': 'Staff Document',
                'verbose_name_plural': 'Staff Documents',
                'ordering': ['staff', 'name', 'created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('created',
                 models.DateTimeField(
                     auto_now_add=True, verbose_name='Created')),
                ('modified',
                 models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('sex',
                 models.CharField(
                     blank=True,
                     choices=[('0', 'Not Known'), ('1', 'Male'),
                              ('2', 'Female'), ('9', 'Not Applicable')],
                     default='0',
                     max_length=1,
                     verbose_name='Gender')),
                ('phone',
                 phonenumber_field.modelfields.PhoneNumberField(
                     blank=True,
                     default='',
                     max_length=128,
                     verbose_name='Phone')),
                ('address',
                 models.TextField(
                     blank=True, default='', verbose_name='Addresss')),
                ('birthday',
                 models.DateField(
                     blank=True,
                     default=None,
                     null=True,
                     verbose_name='Birth day')),
                ('leave_days',
                 models.PositiveIntegerField(
                     blank=True,
                     default=21,
                     help_text='Number of leave days allowed in a year.',
                     verbose_name='Leave days')),
                ('sick_days',
                 models.PositiveIntegerField(
                     blank=True,
                     default=10,
                     help_text='Number of sick days allowed in a year.',
                     verbose_name='Sick days')),
                ('overtime_allowed',
                 models.BooleanField(
                     default=False, verbose_name='Overtime allowed')),
                ('start_date',
                 models.DateField(
                     blank=True,
                     default=None,
                     help_text='The start date of employment',
                     null=True,
                     verbose_name='Start Date')),
                ('end_date',
                 models.DateField(
                     blank=True,
                     default=None,
                     help_text='The end date of employment',
                     null=True,
                     verbose_name='End Date')),
                ('data',
                 django.contrib.postgres.fields.jsonb.JSONField(
                     blank=True, default=dict, verbose_name='Data')),
                ('role',
                 models.ForeignKey(
                     blank=True,
                     default=None,
                     null=True,
                     on_delete=django.db.models.deletion.SET_NULL,
                     to='small_small_hr.Role',
                     verbose_name='Role')),
                ('user',
                 models.OneToOneField(
                     on_delete=django.db.models.deletion.CASCADE,
                     to=settings.AUTH_USER_MODEL,
                     verbose_name='User')),
            ],
            options={
                'verbose_name':
                'Staff Profile',
                'verbose_name_plural':
                'Staff Profiles',
                'ordering': [
                    'user__first_name', 'user__last_name', 'user__username',
                    'created'
                ],
                'abstract':
                False,
            },
        ),
        migrations.AddField(
            model_name='staffdocument',
            name='staff',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='small_small_hr.StaffProfile',
                verbose_name='Staff Member'),
        ),
        migrations.AddField(
            model_name='overtime',
            name='staff',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='small_small_hr.StaffProfile',
                verbose_name='Staff Member'),
        ),
        migrations.AddField(
            model_name='leave',
            name='staff',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='small_small_hr.StaffProfile',
                verbose_name='Staff Member'),
        ),
    ]
