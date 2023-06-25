# Generated by Django 4.2.2 on 2023-06-23 20:31

import datetime
from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal_fields', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), default=['cpf', 'name', 'address', 'value'], size=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SentProposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal_info', models.JSONField(null=True)),
                ('proposal_cpf', models.CharField(max_length=12, verbose_name='CPF')),
                ('created', models.DateTimeField(default=datetime.datetime(2023, 6, 23, 20, 31, 0, 896922, tzinfo=datetime.timezone.utc), verbose_name='Data de Criação')),
                ('answer', models.CharField(choices=[('1', 'Pendente'), ('2', 'Aprovada'), ('3', 'Negada')], default='1', max_length=20, verbose_name='Resposta')),
            ],
        ),
    ]
