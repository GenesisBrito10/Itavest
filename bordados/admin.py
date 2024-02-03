from django.contrib import admin
from .models import Bordado
import requests
from django.contrib.auth.models import Group

class BordadoAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Tamanho', 'Quantidade', 'Status', 'Data', 'user','Telefone')
    search_fields = ('Nome',)
    list_filter = ('Status', 'Tamanho')

    def save_model(self, request, obj, form, change):
     
        obj.user = request.user

      
        original_status = Bordado.objects.get(pk=obj.pk).Status if obj.pk else None

        super().save_model(request, obj, form, change)

        if original_status != obj.Status and obj.Status == 'Pronto':
            
            msg = {
            "message": f"🎉 Prezado(a),\n\nInformamos que o uniforme de {obj.Nome} está pronto para retirada na Loja Itavest Modas! 👮‍♂️👮‍♀️✨ \nEstamos à disposição para atendê-lo(a) e garantir que tudo esteja conforme o esperado.\n\nAguardamos ansiosos por sua vinda.\n\nAtenciosamente,\nEquipe Itavest Modas",
"private": True
            }

            r = requests.post(f'http://37.27.3.154:8005/sendMessage/5562996830458/55{obj.Telefone}', json=msg)
            print(r.status_code)

admin.site.unregister(Group)
admin.site.register(Bordado, BordadoAdmin)
