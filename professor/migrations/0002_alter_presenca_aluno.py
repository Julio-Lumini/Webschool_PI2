# Generated by Django 5.0.4 on 2024-05-19 01:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
        ('secretaria', '0004_turma_alter_cadastro_aluno_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='secretaria.cadastro_aluno'),
        ),
    ]