# Generated by Django 4.2.6 on 2023-11-05 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingresar', '0003_cita'),
    ]

    operations = [
        migrations.CreateModel(
            name='mensaje',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombremensaje', models.CharField(max_length=75)),
                ('telefonomensaje', models.CharField(max_length=8)),
                ('correomensaje', models.EmailField(max_length=254)),
                ('mensajemensaje', models.TextField()),
            ],
        ),
    ]
