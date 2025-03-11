# Generated by Django 5.1.3 on 2025-03-10 17:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0002_alter_recommendation_target'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='asker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='asked_recommendations', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_recommendations', to=settings.AUTH_USER_MODEL),
        ),
    ]
