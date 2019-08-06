# Generated by Django 2.2.2 on 2019-08-05 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataAux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataInicio', models.DateField(blank=True)),
                ('dataFim', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Minuta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('loja', models.CharField(choices=[('TES', 'TES'), ('TEU', 'TEU'), ('TMA', 'TMA'), ('TPI', 'TPI'), ('TMO', 'TMO'), ('TEZ', 'TEZ'), ('TED', 'TED'), ('TPP', 'TPP'), ('TIM', 'TIM'), ('TEC', 'TEC'), ('RTT', 'RTT'), ('TSJ', 'TSJ')], max_length=3, verbose_name='Loja:')),
                ('numMinuta', models.CharField(max_length=7, verbose_name='Minuta:')),
                ('cliente', models.CharField(max_length=150, verbose_name='Cliente:')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('zona', models.CharField(choices=[('SUL', 'SUL'), ('DIRCEU', 'DIRCEU'), ('NORTE', 'NORTE'), ('LESTE', 'LESTE'), ('TIMON', 'TIMON'), ('R.LESTE', 'R.LESTE'), ('R.NORTE', 'R.NORTE'), ('R.SUL', 'R.SUL'), ('R.DIRCEU', 'R.DIRCEU'), ('R.TIMON', 'R.TIMON')], max_length=8, verbose_name='Zona:')),
                ('dataAgendamento', models.DateField(verbose_name='Data de agendamento:')),
                ('turnoAgendamento', models.CharField(choices=[('MANHA', 'MANHA'), ('TARDE', 'TARDE'), ('DURANTE DIA', 'DURANTE DIA')], default='DURANTE DIA', max_length=11, verbose_name='Turno de agendamento:')),
                ('status', models.CharField(blank=True, choices=[('REALIZADO', 'REALIZADO'), ('AGENDADO', 'AGENDADO'), ('CANCELADO', 'CANCELADO')], max_length=9, verbose_name='Status de montagem:')),
            ],
            options={
                'verbose_name': 'Minuta',
                'verbose_name_plural': 'Minutas',
                'ordering': ['id', 'loja', 'numMinuta', 'cliente'],
            },
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zona', models.CharField(choices=[('SUL', 'SUL'), ('DIRCEU', 'DIRCEU'), ('NORTE', 'NORTE'), ('LESTE', 'LESTE'), ('TIMON', 'TIMON'), ('R.LESTE', 'R.LESTE'), ('R.NORTE', 'R.NORTE'), ('R.SUL', 'R.SUL'), ('R.DIRCEU', 'R.DIRCEU'), ('R.TIMON', 'R.TIMON')], max_length=8, verbose_name='Zona:')),
            ],
            options={
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
                'ordering': ['id', 'zona'],
            },
        ),
    ]
