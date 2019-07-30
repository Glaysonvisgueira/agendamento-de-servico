from django.db import models

TIPO_CRP = (
        ('T', 'Estético'),
        ('E', 'Estrutural'),
        ('R', 'Revisão'),        
    )

RECOLHER_PECA = (
        ('1', 'Sim'),
        ('2', 'Não'),        
    )

ZONAS = (
        ('SUL', 'SUL'),
        ('DIRCEU', 'DIRCEU'),
        ('NORTE', 'NORTE'),
        ('LESTE', 'LESTE'),
        ('TIMON', 'TIMON'),
        ('R.LESTE', 'R.LESTE'),
        ('R.NORTE', 'R.NORTE'),
        ('R.SUL', 'R.SUL'),
        ('R.DIRCEU', 'R.DIRCEU'),
        ('R.TIMON', 'R.TIMON'),
    )

STATUS = (
        ('REALIZADO', 'REALIZADO'),
        ('PENDENTE', 'PENDENTE'),
        ('CANCELADO', 'CANCELADO'),        
    )

LOJAS = (
        ('TDC', 'TDC'),
        ('TES', 'TES'),
        ('TEU', 'TEU'),
        ('TMA', 'TMA'),
        ('TPI', 'TPI'),
        ('TMO', 'TMO'),
        ('TEZ', 'TEZ'),
        ('TED', 'TED'),
        ('TPP', 'TPP'),
        ('TIM', 'TIM'),
        ('TEC', 'TEC'),
        ('RTT', 'RTT'),
        ('TSJ', 'TSJ'),
    )

class Crp(models.Model):
    slug = models.SlugField('Loja + Minuta:')
    loja = models.CharField('Loja:', choices=LOJAS,max_length = 3, blank=False)
    numMinuta = models.CharField('Minuta:', max_length = 7, blank=False)
    numCrp = models.CharField('CRP:', max_length = 5, blank=False)
    tipo = models.CharField('Tipo:',choices=TIPO_CRP, max_length = 1, blank=False)
    created_at = models.DateTimeField('Criado em',auto_now_add = True)
    updated_at = models.DateTimeField('Atualizado em',auto_now = True)
    zona = models.CharField('Zona:', choices=ZONAS,max_length = 8, blank=False)
    dataPrevisaoLimite = models.DateField('Data limite para resolução:', blank = False)
    recolhimento = models.CharField('Recolher peça:', choices=RECOLHER_PECA,max_length = 1, blank=False)
    recolhida = models.CharField('Peça recolhida:', choices=RECOLHER_PECA,max_length = 1, blank=True)
    status = models.CharField('Status de montagem:', choices=STATUS,max_length = 9,blank=True,default='PENDENTE')

    def __str__(self):
        return self.loja 

    class Meta:
	    verbose_name = "CRP"
	    verbose_name_plural = "CRP's"
	    ordering = ['loja','numMinuta','numCrp','tipo','zona','dataPrevisaoLimite','recolhimento','recolhida','status']