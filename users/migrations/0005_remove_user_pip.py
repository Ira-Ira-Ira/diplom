# Generated by Django 5.1.6 on 2025-03-10 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pip',
        ),
    ]
