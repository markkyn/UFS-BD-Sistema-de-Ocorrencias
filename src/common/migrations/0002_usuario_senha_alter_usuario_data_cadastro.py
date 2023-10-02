# Generated by Django 4.2.5 on 2023-09-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='senha',
            field=models.CharField(default=None, verbose_name='Senha'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='data_cadastro',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de Cadastro'),
        ),
    ]
