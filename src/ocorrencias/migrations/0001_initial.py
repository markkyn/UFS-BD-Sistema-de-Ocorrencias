# Generated by Django 4.2.5 on 2023-09-29 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datahora_atendimento', models.DateTimeField(verbose_name='Data do Atendimento')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.endereco')),
                ('operadores', models.ManyToManyField(to='common.operacional')),
            ],
        ),
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('atendimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocorrencias.atendimento')),
            ],
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datahora_criacao', models.DateTimeField(auto_now=True, verbose_name='Data de Criação')),
                ('prioridade', models.IntegerField(choices=[(1, 'Urgente'), (2, 'Alta'), (3, 'Media'), (4, 'Baixa'), (5, 'Irrisorio')], default=3)),
                ('observações', models.TextField()),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.solicitante')),
            ],
        ),
    ]