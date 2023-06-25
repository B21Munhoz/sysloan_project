# Generated by Django 4.2.2 on 2023-06-24 06:00

import datetime
from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0002_proposal_delete_sentproposal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proposal',
            old_name='proposal_cpf',
            new_name='cpf',
        ),
        migrations.AlterField(
            model_name='formstructure',
            name='proposal_fields',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), default=['name', 'address', 'value'], size=None),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 24, 6, 0, 30, 861348, tzinfo=datetime.timezone.utc), verbose_name='Data de Criação'),
        ),
    ]