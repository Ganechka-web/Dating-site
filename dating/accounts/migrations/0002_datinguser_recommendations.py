# Generated by Django 5.1.3 on 2025-03-10 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('recommendations', '0002_alter_recommendation_target'),
    ]

    operations = [
        migrations.AddField(
            model_name='datinguser',
            name='recommendations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='recommendations.recommendation'),
        ),
    ]
