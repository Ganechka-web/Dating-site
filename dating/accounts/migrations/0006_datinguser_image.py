# Generated by Django 5.1.3 on 2024-11-18 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_interst_interest'),
    ]

    operations = [
        migrations.AddField(
            model_name='datinguser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/accounts/'),
        ),
    ]
