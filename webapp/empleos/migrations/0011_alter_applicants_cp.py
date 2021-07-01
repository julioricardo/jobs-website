# Generated by Django 3.2.4 on 2021-06-25 14:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleos', '0010_alter_applicants_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicants',
            name='cp',
            field=models.FileField(default='default.png', upload_to='u_cp', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx'])]),
        ),
    ]