# Generated by Django 5.1.2 on 2024-11-27 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_registeredidcardapplication_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='colline',
            name='chief',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chief_of_colline', to='management.colline'),
        ),
        migrations.AddField(
            model_name='commune',
            name='chief',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chief_of_commune', to='management.commune'),
        ),
        migrations.AddField(
            model_name='province',
            name='head',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='head_of_province', to='management.province'),
        ),
    ]
