# Generated by Django 2.2.11 on 2020-03-28 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0038_merge_20200328_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientregistration',
            name='medical_history',
        ),
        migrations.RemoveField(
            model_name='patientregistration',
            name='medical_history_details',
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.IntegerField(choices=[(1, 'NO'), (2, 'Diabetes'), (3, 'Heart Disease'), (4, 'HyperTension'), (5, 'Kidney Diseases')])),
                ('details', models.TextField(blank=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_history', to='facility.PatientRegistration')),
            ],
        ),
    ]
