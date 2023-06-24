class delete:
 def __init__(self,path,name,type):
     self.path=path
     self.name=name
     self.type=type
     self.eliminar()
 def eliminar(self):
     if self.type=="Server":
         print("Eliminando en servidor")
     elif self.type=="Bucket":
         print("Eliminando en Bucket")  