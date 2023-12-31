# Generated by Django 4.2.6 on 2023-11-05 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingresar', '0002_paciente_alter_medicos_colegiado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cita',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fechacita', models.DateField()),
                ('razon', models.TextField()),
                ('diagnostico', models.TextField()),
                ('receta', models.TextField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingresar.medicos')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingresar.paciente')),
            ],
            options={
                'ordering': ['fechacita'],
            },
        ),
    ]
