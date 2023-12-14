# Generated by Django 4.1 on 2023-12-10 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercicios', '0002_alter_exercicio_maquina_and_more'),
        ('clientes', '0001_initial'),
        ('treinadores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade')),
                ('repeticao', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantidade')),
                ('descanso', models.TextField(max_length=100, verbose_name='Descanso')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('exercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercicios.exercicio')),
                ('treinador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treinadores.treinador')),
            ],
            options={
                'verbose_name': 'Treino',
                'verbose_name_plural': 'Treinos',
                'ordering': ['id'],
            },
        ),
    ]