# Generated by Django 2.2.11 on 2020-09-01 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0169_auto_20200830_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientconsultation',
            name='test_id',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
