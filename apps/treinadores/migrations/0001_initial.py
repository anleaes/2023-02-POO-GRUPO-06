# Generated by Django 4.1 on 2023-12-09 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('registro', models.TextField(max_length=100, verbose_name='Registro')),
                ('especialidade', models.TextField(max_length=100, verbose_name='Especialidade')),
                ('email', models.TextField(max_length=100, verbose_name='Email')),
                ('academia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academias.academia')),
            ],
            options={
                'verbose_name': 'Treinador',
                'verbose_name_plural': 'Treinadores',
                'ordering': ['id'],
            },
        ),
    ]
