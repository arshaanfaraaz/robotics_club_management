# Generated by Django 5.1.2 on 2024-10-29 08:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_group_mentor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'permissions': [('view_own_groups', 'Can view own groups')]},
        ),
        migrations.AlterField(
            model_name='group',
            name='mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mentored_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]