# Generated by Django 4.2.4 on 2023-08-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_doctor_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='answer',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
