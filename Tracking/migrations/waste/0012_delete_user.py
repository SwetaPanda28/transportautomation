# Generated by Django 4.0.2 on 2022-03-05 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tracking', '0011_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]