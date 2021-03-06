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
        
        
class User(models.Model):
    id = models.IntegerField()
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user'


class Company(models.Model):
    companyid = models.AutoField(primary_key=True)  
    companyname = models.CharField(max_length=255)  
    companyaddress1 = models.CharField(max_length=255)
    companyaddress2 = models.CharField(max_length=255)
    companycity = models.CharField(max_length=255)
    companypostalcode = models.CharField(max_length=255)
    companystate = models.CharField(max_length=255)  
    companycountry = models.CharField(max_length=255)
    companyphonenumber = models.IntegerField()  
    user = models.ForeignKey("User",on_delete=models.CASCADE)
    numberofvehicles = models.IntegerField()
    companybaselat = models.FloatField()  
    companybaselong = models.FloatField()  
    
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


class Vehicle(models.Model):
    vehiclename = models.CharField(db_column='vehicleName', max_length=255)  # Field name made lowercase.
    vehicledriver = models.CharField(db_column='vehicleDriver', max_length=255)  # Field name made lowercase.
    vehicletype = models.CharField(db_column='vehicleType', max_length=255)  # Field name made lowercase.
    vehiclemilage = models.IntegerField(db_column='vehicleMilage')  # Field name made lowercase.
    companyid = models.ForeignKey(Company, models.DO_NOTHING, db_column='companyID',blank=True)  # Field name made lowercase.
    vehicleid = models.IntegerField(db_column='vehicleID', primary_key=True,blank=True)  # Field name made lowercase.
    registationid = models.IntegerField(db_column='registrationid')
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
