# Generated by Django 3.2.7 on 2021-09-27 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagement', '0008_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='is_approved',
            field=models.BooleanField(default=False, max_length=100),
        ),
    ]
