# Generated by Django 4.2.1 on 2023-06-15 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsAdmin', '0005_alter_attendance_attendance_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='classes',
            field=models.CharField(max_length=100),
        ),
    ]