# Generated by Django 3.2.4 on 2021-06-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('parcial', 'TIEMPO PARCIAL'), ('completo', 'TIEMPO COMPLETO'), ('remoto', 'REMOTO')], default='empleo', max_length=30)),
                ('categoria', models.CharField(choices=[('pasantia', 'PASANTIA'), ('empleo', 'EMPLEO'), ('voluntariado', 'VOLUNTARIADO'), ('otro', 'OTRO')], default='completo', max_length=30)),
                ('zona', models.CharField(choices=[('costa', 'COSTA'), ('sierra', 'SIERRA'), ('oriente', 'ORIENTE'), ('galapagos', 'GALAPAGOS')], default='sierra', max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('salario', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=300)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_cierre', models.DateField()),
                ('activo', models.BooleanField(default=False)),
            ],
        ),
    ]