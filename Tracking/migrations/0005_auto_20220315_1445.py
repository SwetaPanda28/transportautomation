# Generated by Django 2.0 on 2022-03-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracking', '0004_auto_20220315_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensingdata',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sensingdata',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]