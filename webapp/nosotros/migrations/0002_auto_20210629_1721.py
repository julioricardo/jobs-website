# Generated by Django 2.2.24 on 2021-06-29 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nosotros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]