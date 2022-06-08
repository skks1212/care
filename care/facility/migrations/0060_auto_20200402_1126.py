# Generated by Django 2.2.11 on 2020-04-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0059_patientsample_fast_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='facility_type',
            field=models.IntegerField(choices=[(1, 'Educational Inst'), (2, 'Private Hospital'), (3, 'Other'), (4, 'Hostel'), (5, 'Hotel'), (6, 'Lodge'), (7, 'TeleMedicine'), (7, 'Govt Hospital')]),
        ),
    ]
