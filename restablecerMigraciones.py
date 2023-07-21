import os

#Con esta libreria eliminamos carpetas que contienen elementos
from shutil import rmtree

Aplicaciones = os.listdir("./aplicaciones")
print(Aplicaciones)
print("\n\n")
print(os.listdir())
print("--------------------------")
print(os.listdir("./aplicaciones"))

print("---------------------------")

for elemento in os.listdir("./aplicaciones"):

    #print("./aplicaciones/"+elemento)
    if os.path.isdir("./aplicaciones/"+elemento):
        #print(elemento, "Es una carpeta")

        #Comprobamos si existen las carpetas de migrations
        if os.path.isdir("./aplicaciones/"+elemento+"/migrations"):
            #print("Aqui hay carpetas migrations")
            rmtree("./aplicaciones/"+elemento+"/migrations")
        #print(elemento," ",os.path.isdir("./aplicaciones2/"+elemento+"/migrations"))


for elemento in os.listdir("./aplicaciones"):

    #print("./aplicaciones/"+elemento)
    if os.path.isdir("./aplicaciones/"+elemento):
        print(elemento, "Es una carpeta")
        #asi creamos carpetas
        os.mkdir("./aplicaciones/"+elemento+"/migrations")
        os.mkdir("./aplicaciones/"+elemento+"/migrations/"+"__pycache__")

        #asi creamos archivos
        f = open ("./aplicaciones/"+elemento+"/migrations/"+"__init__.py","w")
        #f.write('hola mundo')
        f.close()

    else:
        print(elemento," Es un archivo")


