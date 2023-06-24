class rename:
 def __init__(self, path, name, type):
     self.name = name
     self.type = type
     self.pathe = path
     self.renombrar()


 def renombrar(self):
     if self.type=="Server":
         print("Renombrando en servidor")
     elif self.type=="Bucket":
         print("Renombrando en Bucket")