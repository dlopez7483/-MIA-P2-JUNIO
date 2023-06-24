
class Create:
 def __init__(self,name,body,type,path):
     self.name=name
     self.body=body
     self.type=type
     self.path=path
     self.crear()
 
 def crear(self):
     if self.type=="Server":
         print("Creando en servidor")
     elif self.type=="Bucket":
         print("Creando en Bucket")