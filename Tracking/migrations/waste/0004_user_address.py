# Generated by Django 4.0.2 on 2022-02-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracking', '0003_user_alter_company_user_delete_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]