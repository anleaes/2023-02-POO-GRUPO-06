# Generated by Django 4.1 on 2023-12-09 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('nutricionistas', '0002_alter_nutricionista_email_and_more'),
        ('alimentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planoalimentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horariosRefeicoes', models.CharField(max_length=50, verbose_name='Nome')),
                ('alimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alimentos.alimento')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('nutricionista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutricionistas.nutricionista')),
            ],
            options={
                'verbose_name': 'Planoalimentar',
                'verbose_name_plural': 'Planosalimentares',
                'ordering': ['id'],
            },
        ),
    ]
