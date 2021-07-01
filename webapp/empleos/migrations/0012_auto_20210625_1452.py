# Generated by Django 3.2.4 on 2021-06-25 14:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleos', '0011_alter_applicants_cp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicants',
            name='cp',
            field=models.FileField(default='default.png', upload_to='cp', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx'])]),
        ),
        migrations.AlterField(
            model_name='applicants',
            name='cv',
            field=models.FileField(default='default.png', upload_to='cv', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx'])]),
        ),
    ]
