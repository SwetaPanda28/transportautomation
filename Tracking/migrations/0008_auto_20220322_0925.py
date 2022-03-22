# Generated by Django 2.0 on 2022-03-22 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tracking', '0007_auto_20220316_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='vehicle',
        ),
        migrations.RemoveField(
            model_name='sensingdata',
            name='device',
        ),
        migrations.RemoveField(
            model_name='user',
            name='company',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='company',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Device',
        ),
        migrations.DeleteModel(
            name='Sensingdata',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]