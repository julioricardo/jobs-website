# Generated by Django 3.2.4 on 2021-06-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizaciones', '0002_alter_orgprofile_ruc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgprofile',
            name='activo',
            field=models.BooleanField(default=False),
        ),
    ]