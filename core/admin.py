from django.contrib import admin

from montagem.models import Minuta, Zona

class MinutaAdmin(admin.ModelAdmin):

	list_display = ['id','loja','numMinuta','cliente','dataAgendamento','zona','turnoAgendamento','status']
	search_fields =['loja','numMinuta','cliente','dataAgendamento','zona','turnoAgendamento','status']	

admin.site.register(Minuta, MinutaAdmin)	