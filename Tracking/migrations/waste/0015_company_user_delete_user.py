# Generated by Django 4.0.2 on 2022-03-07 04:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tracking', '0014_remove_company_user_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]