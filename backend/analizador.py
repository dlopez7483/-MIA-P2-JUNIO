import re
class analizador:
 def __init__(self,linea):
     self.linea=linea
     self.comandos=[]


 def instruccion(self):
     patron=r"(Create|Delete|Copy|Transfer|Rename|Modify|Backup|Recovery|delete_all|Open)"
     match=re.match(patron,self.linea,re.I)
     if match:
         return re.search(patron,self.linea,re.I)[0]
     else:
         return None
 def comandos_ (self):
     patron=r"(Create|Delete|Copy|Transfer|Rename|Modify|Backup|Recovery|delete_all|Open)"
     line=re.sub(patron,"",self.linea,re.I)
     patron2 = r"-(\w+)->([^->]+)"
     self.comandos = re.findall(patron2, line)
     return self.comandos
 

class analisis:
 def __init__(self,linea):
     self.linea=linea
 def iniciar_comandos(self):
     a=analizador(self.linea)
     ins=a.instruccion()
     comandos_a_modificar=a.comandos_()
     comandos_a_modificar_2 = [(c[0], re.sub(r'"', '', c[1])) for c in comandos_a_modificar]
     comands=[(c[0], re.sub(r'\s+$','', c[1])) for c in comandos_a_modificar_2]

     