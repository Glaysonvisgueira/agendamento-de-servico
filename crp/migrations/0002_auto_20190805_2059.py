# Generated by Django 2.2.2 on 2019-08-05 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crp',
            name='dataRecebimentoDocumento',
        ),
        migrations.AddField(
            model_name='crp',
            name='dataRecebimentoCrpEntrega',
            field=models.DateField(blank=True, null=True, verbose_name='Data de envio para setor de entrega:'),
        ),
    ]