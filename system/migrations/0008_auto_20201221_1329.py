# Generated by Django 3.1.2 on 2020-12-21 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system', '0007_auto_20201218_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='maker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]