# Generated by Django 5.1.3 on 2025-03-10 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_datinguser_recommendations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datinguser',
            name='recommendations',
        ),
    ]
