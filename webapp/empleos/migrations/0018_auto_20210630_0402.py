# Generated by Django 2.2.24 on 2021-06-30 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleos', '0017_auto_20210629_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobs',
            options={'ordering': ['-fecha_publicacion']},
        ),
    ]
