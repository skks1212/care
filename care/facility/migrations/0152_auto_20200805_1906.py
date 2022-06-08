# Generated by Django 2.2.11 on 2020-08-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0151_auto_20200802_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpatientregistration',
            name='ip_no',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='patientconsultation',
            name='diagnosis',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='patientregistration',
            name='ip_no',
            field=models.CharField(default='', max_length=100),
        ),
    ]
