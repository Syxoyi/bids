# Generated by Django 3.1.2 on 2021-01-12 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0011_auto_20210112_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='time_creation',
            field=models.DateTimeField(null=True),
        ),
    ]