# Generated by Django 2.2.11 on 2021-06-23 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facility', '0257_auto_20210618_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilitycapacity',
            name='room_type',
            field=models.IntegerField(choices=[(0, 'Total'), (2, 'Hostel'), (3, 'Single Room with Attached Bathroom'), (40, 'KASP Beds'), (50, 'KASP ICU beds'), (60, 'KASP Oxygen beds'), (70, 'KASP Ventilator beds'), (1, 'General Bed'), (10, 'ICU'), (20, 'Ventilator'), (30, 'Covid Beds'), (100, 'Covid Ventilators'), (110, 'Covid ICU'), (120, 'Covid Oxygen beds'), (150, 'Oxygen beds')]),
        ),
        migrations.AlterField(
            model_name='historicalfacilitycapacity',
            name='room_type',
            field=models.IntegerField(choices=[(0, 'Total'), (2, 'Hostel'), (3, 'Single Room with Attached Bathroom'), (40, 'KASP Beds'), (50, 'KASP ICU beds'), (60, 'KASP Oxygen beds'), (70, 'KASP Ventilator beds'), (1, 'General Bed'), (10, 'ICU'), (20, 'Ventilator'), (30, 'Covid Beds'), (100, 'Covid Ventilators'), (110, 'Covid ICU'), (120, 'Covid Oxygen beds'), (150, 'Oxygen beds')]),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.IntegerField(choices=[(0, 'Total'), (2, 'Hostel'), (3, 'Single Room with Attached Bathroom'), (40, 'KASP Beds'), (50, 'KASP ICU beds'), (60, 'KASP Oxygen beds'), (70, 'KASP Ventilator beds'), (1, 'General Bed'), (10, 'ICU'), (20, 'Ventilator'), (30, 'Covid Beds'), (100, 'Covid Ventilators'), (110, 'Covid ICU'), (120, 'Covid Oxygen beds'), (150, 'Oxygen beds')]),
        ),
        migrations.CreateModel(
            name='ShiftingRequestComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('comment', models.TextField(blank=True, default='')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facility.ShiftingRequest')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
