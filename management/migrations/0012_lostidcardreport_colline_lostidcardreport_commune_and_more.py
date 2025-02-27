# Generated by Django 5.1.2 on 2024-11-27 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_remove_lostidcardreport_citizen_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostidcardreport',
            name='colline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.colline'),
        ),
        migrations.AddField(
            model_name='lostidcardreport',
            name='commune',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.commune'),
        ),
        migrations.AddField(
            model_name='lostidcardreport',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='lostidcardreport',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.province'),
        ),
        migrations.AddField(
            model_name='registeredidcardapplication',
            name='colline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.colline'),
        ),
        migrations.AddField(
            model_name='registeredidcardapplication',
            name='commune',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.commune'),
        ),
        migrations.AddField(
            model_name='registeredidcardapplication',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.province'),
        ),
    ]
