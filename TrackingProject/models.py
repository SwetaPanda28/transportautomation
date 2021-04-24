# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Company(models.Model):
    companyid = models.IntegerField(db_column='companyID', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='companyName', max_length=255)  # Field name made lowercase.
    companyaddress1 = models.CharField(db_column='companyAddress1', max_length=255)  # Field name made lowercase.
    companyaddress2 = models.CharField(db_column='companyAddress2', max_length=255)  # Field name made lowercase.
    companycity = models.CharField(db_column='companyCity', max_length=255)  # Field name made lowercase.
    companypostalcode = models.CharField(db_column='companyPostalCode', max_length=255)  # Field name made lowercase.
    companystate = models.CharField(db_column='companyState', max_length=255)  # Field name made lowercase.
    companycountry = models.CharField(db_column='companyCountry', max_length=255)  # Field name made lowercase.
    companyphonenumber = models.IntegerField(db_column='companyPhoneNumber')  # Field name made lowercase.
    username = models.ForeignKey('User', models.DO_NOTHING, db_column='username')
    numberofvehicles = models.IntegerField(db_column='numberOfVehicles')  # Field name made lowercase.
    companybaselat = models.FloatField(db_column='companyBaseLat')  # Field name made lowercase.
    companybaselong = models.FloatField(db_column='companyBaseLong')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company'


class Device(models.Model):
    imienumber = models.CharField(primary_key=True, max_length=255)
    serialno = models.CharField(max_length=255)
    companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='companyID')  # Field name made lowercase.
    vehicleid = models.ForeignKey('Vehicle', models.DO_NOTHING, db_column='vehicleID')  # Field name made lowercase.
    msisdn = models.BigIntegerField(db_column='MSISDN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'device'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class User(models.Model):
    id = models.IntegerField()
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user'


class Vehicle(models.Model):
    vehiclename = models.CharField(db_column='vehicleName', max_length=255)  # Field name made lowercase.
    vehicledriver = models.CharField(db_column='vehicleDriver', max_length=255)  # Field name made lowercase.
    vehicletype = models.CharField(db_column='vehicleType', max_length=255)  # Field name made lowercase.
    vehiclemilage = models.IntegerField(db_column='vehicleMilage')  # Field name made lowercase.
    companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='companyID')  # Field name made lowercase.
    vehicleid = models.IntegerField(db_column='vehicleID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vehicle'


class Warehouse(models.Model):
    insertdate = models.DateTimeField(db_column='insertDate')  # Field name made lowercase.
    generateddate = models.DateTimeField(db_column='generatedDate')  # Field name made lowercase.
    latitude = models.FloatField()
    longitude = models.FloatField()
    imienumber = models.ForeignKey(Device, models.DO_NOTHING, db_column='imienumber')

    class Meta:
        managed = False
        db_table = 'warehouse'
