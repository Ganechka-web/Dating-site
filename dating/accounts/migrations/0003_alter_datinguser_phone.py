# Generated by Django 5.1.3 on 2024-11-18 11:35

import accounts.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_datinguser_interests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datinguser',
            name='phone',
            field=accounts.fields.PhoneField(blank=True, null=True),
        ),
    ]
