# Generated by Django 3.2.4 on 2021-06-14 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgprofile',
            name='ruc',
            field=models.CharField(blank=True, default='9999999999', max_length=13, null=True, verbose_name='RUC'),
        ),
    ]
