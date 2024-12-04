# Generated by Django 5.1.3 on 2024-12-03 08:02

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_alter_chat_id_alter_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
