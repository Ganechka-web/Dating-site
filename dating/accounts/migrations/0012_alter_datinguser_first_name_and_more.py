# Generated by Django 5.1.3 on 2024-12-24 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_datinguser_accounts_da_age_22cf45_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datinguser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='datinguser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
