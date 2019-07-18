# Generated by Django 2.2.2 on 2019-07-11 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('montagem', '0004_remove_minuta_solicitanteagendamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minuta',
            name='loja',
            field=models.CharField(choices=[('TES', 'TES'), ('TEU', 'TEU'), ('TMA', 'TMA'), ('TPI', 'TPI'), ('TMO', 'TMO'), ('TEZ', 'TEZ'), ('TED', 'TED'), ('TPP', 'TPP'), ('TIM', 'TIM'), ('TEC', 'TEC'), ('RTT', 'RTT'), ('TSJ', 'TSJ')], max_length=3, verbose_name='Loja:'),
        ),
        migrations.AlterField(
            model_name='minuta',
            name='numMinuta',
            field=models.CharField(max_length=7, verbose_name='Minuta:'),
        ),
        migrations.AlterField(
            model_name='minuta',
            name='turnoAgendamento',
            field=models.CharField(choices=[('MANHA', 'MANHA'), ('TARDE', 'TARDE'), ('DURANTE DIA', 'DURANTE DIA')], max_length=8, verbose_name='Turno de agendamento:'),
        ),
        migrations.AlterField(
            model_name='minuta',
            name='zona',
            field=models.CharField(choices=[('SUL', 'SUL'), ('DIRCEU', 'DIRCEU'), ('NORTE', 'NORTE'), ('LESTE', 'LESTE'), ('TIMON', 'TIMON'), ('R.LESTE', 'R.LESTE'), ('R.NORTE', 'R.NORTE'), ('R.SUL', 'R.SUL'), ('R.DIRCEU', 'R.DIRCEU'), ('R.TIMON', 'R.TIMON')], max_length=8, verbose_name='Zona:'),
        ),
    ]