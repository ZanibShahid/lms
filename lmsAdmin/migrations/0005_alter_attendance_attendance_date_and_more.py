# Generated by Django 4.2.1 on 2023-06-15 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsAdmin', '0004_alter_attendance_classes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.CharField(max_length=89),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_time',
            field=models.CharField(max_length=70),
        ),
    ]
