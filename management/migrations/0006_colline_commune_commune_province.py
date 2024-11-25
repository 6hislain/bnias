# Generated by Django 5.1.2 on 2024-11-25 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_alter_publication_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='colline',
            name='commune',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.commune'),
        ),
        migrations.AddField(
            model_name='commune',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.province'),
        ),
    ]
