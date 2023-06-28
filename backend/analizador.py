import re
from Create import Create
from flask import  jsonify
from delete import delete
from copiar import copiar
from transfer import transfer
from renombrar import renombrar
from modify import Modify
from backup import backup
from recovery import recovery
from delete_all import delete_all
from abrir import abrir
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
     if(re.match("Create",ins,re.I)):
         name=""
         body=""
         type=""
         path=""
         for c in comands:
             if (re.match("name",c[0],re.I)):
                 name=c[1]
             elif (re.match("body",c[0],re.I)):
                 body=c[1]
             elif (re.match("path",c[0],re.I)):
                 path=c[1]
             elif (re.match("type",c[0],re.I)):
                 if(re.match("server",c[1],re.I)):
                     type="Server"
                 elif(re.match("bucket",c[1],re.I)):
                     type="Bucket"
         if(name!="" and body!="" and type!="" and path!=""):
             c=Create(name,body,type,path)
             return c.crear()
         else:
             return "Error en los parametros de crear"
     elif(re.match("Delete",ins,re.I)):
         path=""
         name=""
         type=""
         for c in comands:
             if (re.match("path",c[0],re.I)):
                 path=c[1]
             elif (re.match("name",c[0],re.I)):
                 name=c[1]
             elif (re.match("type",c[0],re.I)):
                 if(re.match("server",c[1],re.I)):
                     type="Server"
                 elif(re.match("bucket",c[1],re.I)):
                     type="Bucket"
         if(path!="" and type!=""):
             d=delete(path,name,type)
         else:
             return "Error en los parametros de eliminar"
     elif(re.match("Copy",ins,re.I)):
         from_=""
         to=""
         type_to=""
         type_from=""
         for c in comands:
             if (re.match("from",c[0],re.I)):
                    from_=c[1]
             elif (re.match("to",c[0],re.I)):
                    to=c[1]
             elif (re.match("type_to",c[0],re.I)):
                 if(re.match("server",c[1],re.I)):
                     type_to="Server"
                 elif(re.match("bucket",c[1],re.I)):
                     type_to="Bucket"
             elif (re.match("type_from",c[0],re.I)):
                 if(re.match("server",c[1],re.I)):
                     type_from="Server"
                 elif(re.match("bucket",c[1],re.I)):
                     type_from="Bucket"
         if(from_!="" and to!="" and type_to!="" and type_from!=""):
             c=copiar(from_,to,type_to,type_from)
             return c.copiar_()
         else:
             return "Error en los parametros de copiar"
     elif(re.match("Transfer",ins,re.I)):
         from_=""
         to=""
         type_to=""
         type_from=""
         for c in comands:
             if (re.match("from",c[0],re.I)):
                 from_=c[1]
             elif (re.match("to",c[0],re.I)):
                 to=c[1]
             elif (re.match("type_to",c[0],re.I)):
                 if(re.match("server",c[1],re.I)):
                        type_to="Server"
                 elif(re.match("bucket",c[1],re.I)):
                        type_to="Bucket"
             elif (re.match("type_from",c[0],re.I)):
                 if(re.match("server",c[1],re.I)):
                        type_from="Server"
                 elif(re.match("bucket",c[1],re.I)):
                        type_from="Bucket"
         if(from_!="" and to!="" and type_to!="" and type_from!=""):
             t=transfer(from_,to,type_to,type_from)
             return t.transfer_()
         else:
             return "Error en los parametros de transferir"
     elif(re.match("Rename",ins,re.I)):
         path="" 
         name = ""
         type=""
         for c in comands:
             if (re.match("path",c[0],re.I)):
                     path=c[1]
             elif (re.match("name",c[0],re.I)):
                     name=c[1]
             elif (re.match("type",c[0],re.I)):
                 if(re.match("server",c[1],re.I)):
                     type="Server"
                 elif(re.match("bucket",c[1],re.I)):
                     type="Bucket"  

         if(path!="" and name!="" and type!=""):
             r=renombrar(path,name,type)
             return r.renombrar()
         else:
             return "Error en los parametros de renombrar"
     elif(re.match("Modify",ins,re.I)):
         path=""
         body=""
         type=""
         for c in comands:
             if (re.match("path",c[0],re.I)):
                 path=c[1]
             elif (re.match("body",c[0],re.I)):
                 body=c[1]
             elif (re.match("type",c[0],re.I)):
                 if(re.match("server",c[1],re.I)):
                     type="Server"
                 elif(re.match("bucket",c[1],re.I)):
                     type="Bucket" 
         if(path!="" and body!="" and type!=""):
             m=Modify(body,type,path)
             return m.modificar()
         else:
             return "Error en los parametros de modificar"
     elif(re.match("Backup",ins,re.I)):
         type_to=""
         type_from=""
         ip=""
         port=""
         name=""
         for c in comands:
             if (re.match("type_to",c[0],re.I)):
                 if(re.match("server",c[1],re.I)):
                     type_to="Server"
                 elif(re.match("bucket",c[1],re.I)):
                     type_to="Bucket"
             elif (re.match("type_from",c[0],re.I)):
                 if(re.match("server",c[1],re.I)):
                     type_from="Server"
                 elif(re.match("bucket",c[1],re.I)):
                     type_from="Bucket"
             elif (re.match("ip",c[0],re.I)):
                 ip=c[1]
             elif (re.match("port",c[0],re.I)):
                 port=c[1]
             elif (re.match("name",c[0],re.I)):
                 name=c[1]
         if(type_to!="" and type_from!="" and name!=""):
             b=backup(type_to,type_from,ip,port,name)
             return b.backup_()
         else:
                return "Error en los parametros de backup"
     elif(re.match("Recovery",ins,re.I)):
         type_to=""
         type_from=""
         ip=""
         port=""
         name=""
         for c in comands:
             if (re.match("type_to",c[0],re.I)):
                 if(re.match("server",c[1],re.I)):
                     type_to="Server"
                 elif(re.match("bucket",c[1],re.I)):
                     type_to="Bucket"
             elif (re.match("type_from",c[0],re.I)):
                 if(re.match("server",c[1],re.I)):
                     type_from="Server"
                 elif(re.match("bucket",c[1],re.I)):
                     type_from="Bucket"
             elif (re.match("ip",c[0],re.I)):
                 ip=c[1]
             elif (re.match("port",c[0],re.I)):
                 port=c[1]
             elif (re.match("name",c[0],re.I)):
                 name=c[1]
         if(type_to!="" and type_from!="" and name!=""):
             r=recovery(type_to,type_from,ip,port,name)
             return r.recovery_()
         else:
             return "Error en los parametros de recovery"
     elif(re.match("delete_all",ins,re.I)):
         type=""
         for c in comands:
             if (re.match("type",c[0],re.I)):
                 if(re.match("server",c[1],re.I)):
                     type="Server"
                 elif(re.match("bucket",c[1],re.I)):
                     type="Bucket"
         if(type!=""):
             d=delete_all(type)
             return d.delete_all_()
         else:
             return "Error en los parametros de eliminar todo"
     elif(re.match("Open",ins,re.I)):
         type=""
         ip=""
         port=""
         name=""
         for c in comands:
             if (re.match("type",c[0],re.I)):
                 if(re.match("server",c[1],re.I)):
                     type="Server"
                 elif(re.match("bucket",c[1],re.I)):
                     type="Bucket"
             elif (re.match("ip",c[0],re.I)):
                 ip=c[1]
             elif (re.match("port",c[0],re.I)):
                 port=c[1]
             elif (re.match("name",c[0],re.I)):
                 name=c[1]
         if(type!="" and name!=""):
             a=abrir(type,ip,port,name)
             return a.abrir_()
         else:
             return "Error en los parametros de abrir"
     else:
         return "Error en la instrucción."

              
        
     