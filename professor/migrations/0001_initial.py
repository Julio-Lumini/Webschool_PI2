# Generated by Django 5.0.4 on 2024-05-18 22:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('secretaria', '0004_turma_alter_cadastro_aluno_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('presente', models.BooleanField(default=False)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secretaria.cadastro_aluno')),
            ],
        ),
    ]
