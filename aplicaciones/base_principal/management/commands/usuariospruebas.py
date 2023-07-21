from django.core.management.base import BaseCommand, CommandError

#Aqui esta el modelo de los Usuarios
from aplicaciones.usuarios.models import Usuarios

#Aqui esta el modelo para crear discipulos

class Command(BaseCommand):
    help = 'comando para crear usuarios de pruebas'

    def handle(self, *args, **options):


        #Creamos al usuario admin
        #Usuario Warlis Zapata
        admin = Usuarios(username="admin",nombres="admin",apellidos="admin",email="admin@gmail.com",cedula="000000000",activo=True,is_superuser=True,admin=True,direccion="desconocido",sucursal=None,cobertura = None,telefono="00000000000")
        admin.set_password("admin")
        admin.save()


        #Creamos los usuarios de prueba

        #Los primeros tres usuarios son los pastores congregacionales

        #Usuario Warlis Zapata
        warlis = Usuarios(username="warlis",nombres="warlis",apellidos="zapata",email="warlis@gmail.com",cedula="12322212",activo=True,is_superuser=False,admin=False,direccion="antimano",telefono="04167156325")
        warlis.set_password("warlis")
        warlis.save()

        #Usuario Josue Arevalo
        josue = Usuarios(username="josue",nombres="josue",apellidos="arevalo",email="josue@gmail.com",cedula="11652212",activo=True,is_superuser=False,admin=False,direccion="las adjuntas",telefono="04247156325")
        josue.set_password("josue")
        josue.save()

        #Usuario Luis Cedeño
        luis = Usuarios(username="luis",nombres="luis",apellidos="cedeño",email="luis@gmail.com",cedula="18676512",activo=True,is_superuser=False,admin=False,direccion="caricuao",telefono="04263356325")
        luis.set_password("luis")
        luis.save()




        
        
        
        self.stdout.write(self.style.HTTP_SUCCESS("USUARIOS CREADOS CON EXITO"))
        #self.stdout.write(self.style.WARNING("Texto de advertencia"))