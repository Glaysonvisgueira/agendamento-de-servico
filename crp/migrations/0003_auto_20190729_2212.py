# Generated by Django 2.2.2 on 2019-07-30 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crp', '0002_auto_20190728_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='crp',
            name='slug',
            field=models.SlugField(default='', verbose_name='Loja + Minuta:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='crp',
            name='loja',
            field=models.CharField(choices=[('TDC', 'TDC'), ('TES', 'TES'), ('TEU', 'TEU'), ('TMA', 'TMA'), ('TPI', 'TPI'), ('TMO', 'TMO'), ('TEZ', 'TEZ'), ('TED', 'TED'), ('TPP', 'TPP'), ('TIM', 'TIM'), ('TEC', 'TEC'), ('RTT', 'RTT'), ('TSJ', 'TSJ')], max_length=3, verbose_name='Loja:'),
        ),
        migrations.AlterField(
            model_name='crp',
            name='status',
            field=models.CharField(blank=True, choices=[('REALIZADO', 'REALIZADO'), ('PENDENTE', 'PENDENTE'), ('CANCELADO', 'CANCELADO')], max_length=9, verbose_name='Status de montagem:'),
        ),
    ]
