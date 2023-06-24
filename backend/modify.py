class Modify:
 def __init__(self,body,type,path):
     self.body=body
     self.type=type
     self.path=path
     self.modificar()
 def modificar(self):
     if self.type=="Server":
         print("Modificando en servidor")
     elif self.type=="Bucket":
         print("Modificando en Bucket")