import os
import shutil #libreria para borrar carpetas esten o no llenas
from django.conf import settings
from garageclub.settings import MEDIA_URL, STATIC_URL, AUTH_USER_MODEL
from django.db import models

#Estos dos modelos son para crear permisos personalizados
from django.contrib.auth.models import Permission,Group
from django.contrib.contenttypes.models import ContentType


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete




# Create your models here.

##################################################################################################
####################### Modelos para Usuarios ####################################################


class UsuarioManager(BaseUserManager):

    def create_user(self,email,username, password=None, admin = False,is_superuser =False,rol = "creyente"):
        print("Creamos Usuario Normal")
        #if not email:
        #    raise ValueError('El usuario debe tener un correo electronico')

        usuario = self.model(
            
            username = username,
            rol = rol,
            email = self.normalize_email(email),
            password = password,
            #admin =admin,
            #is_superuser = is_superuser,
        )

        #aqui encriptamos la clave para no guardar en texto plano
        print("ENCRIPTAMOS", password)
        usuario.set_password(password)
        usuario.admin = admin
        usuario.is_superuser = is_superuser
        usuario.save()
        return usuario
    
    

    #Funcion para usuario administrador
    def create_superuser(self,email,username,password,rol="master"):
        print("Creamos superusuario")

        usuario = self.model(
            
            username = username,
            #rol = rol,
            email = self.normalize_email(email),
            password = password,
            #admin =admin,
            #is_superuser = is_superuser,
        )
        """
        usuario = self.create_user(
            email = email,  
            username = username,
            password = password,
            admin =admin,
            is_superuser = is_superuser
        )
        """

        print("ENCRIPTAMOS EN SUPERUSER", password)
        usuario.set_password(password)
        usuario.is_superuser = True #Es superusuario
        usuario.admin = True #Acceso a todo
        usuario.tipo_usuario = "master"
        usuario.save()
        return usuario


#Funcion para agregar carpetas al usuario
def foto_perfil_usuarios(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    print(instance)
    print(instance.id)
    print(instance.username)
    return 'usuarios/{0}/perfil/{1}'.format(instance.username, filename)






class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,unique=True)

    def __str__(self):
         return str(self.nombre)

    class Meta:

        verbose_name = "Rol"
        verbose_name_plural = "Roles"

        permissions = [
            #Para ver los informes
            #("informejugada", "InformeJugada"),

        ]#Fin de los permisos
        







# Heredamos de AbstractBaseUser para adaptarlo a nuestro gusto
class Usuarios(AbstractBaseUser,PermissionsMixin):

    #(Lo que se guarda en bases de datos, lo que se ve al usuario)
    tipo_usuario = [
        
        ('master','Master'),
        ('administrador','Administrador'),
        ('normal','Normal'),
    ]



    nacionalidad = [
        
        ('venezolano','Venezolano'),
        ('extranjero','Extranjero'),
    ]

    #tipo_plan = [
    #    ('gratis','Free'),
    #    ('pago','Pay'),
    #]
    

    id = models.AutoField(primary_key=True)

    #Este campo sera para ingresar al sistema
    username = models.CharField("Username",max_length=200,unique=True)

    #Informacion general del usuario
    nombres = models.CharField("Nombres",max_length=200,blank=True, null=True) 
    apellidos = models.CharField("Apellidos",max_length=200,blank=True, null=True) 
    email = models.EmailField("Correo Electronico",max_length=150, unique=True)
    cedula = models.IntegerField(default=0,blank=True, null=True)
    #empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE,blank=True, null=True)

    #Referente al sistema
    activo = models.BooleanField(default=True)#Para poder ingresar al sistema  
    is_superuser = models.BooleanField(default=False)#Este es superusuario
    admin = models.BooleanField(default=False)#Para poder ingresar al admin de django
    
    fecha_creacion = models.DateTimeField(auto_now_add=True) 
    ultimo_ingreso = models.DateTimeField('fecha ultimo ingreso', auto_now=True)
    direccion = models.CharField("Direccion",max_length=100,blank=True, null=True,default="Desconocido") 
    imagenPerfil = models.ImageField("Imagen de Perfil", upload_to=foto_perfil_usuarios,default="media/perfil/default.png", max_length=200,blank=True,null=True)



    tipo_usuario = models.CharField("tipo Usuario",max_length=150,choices=tipo_usuario,default='normal',blank=True, null=True)
    nacionalidad = models.CharField("Nacionalidad",max_length=150,choices=nacionalidad,default='venezolano',blank=False, null=True)
    #rol = models.ForeignKey(Rol,on_delete=models.CASCADE,blank=False, null=True)
    #rol = models.CharField("Rol",max_length=150,choices=usuario_tipos,default='cliente',blank=True, null=True)

    telefono = models.CharField("Telefono", max_length=50,blank=True,null=True,default="04242020470")
    #imagenFondoEscritorio = models.ImageField("Imagen de Escritorio", upload_to=direccion_usuarios, max_length=200,blank=True,null=True)
    
    #Para enlazar al manager que has creado
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'  #Para estableccer este campo como unico
    REQUIRED_FIELDS = ['email'] # Campos obligatorios(los pide cuando los creas por consola)

    def __str__(self):
        return f'Usuario {self.username}'

    def obtenerImagenPerfil(self):
      
        if self.imagenPerfil:
            return '{}{}'.format(MEDIA_URL,self.imagenPerfil)
        return '{}{}'.format(MEDIA_URL,'perfil/default.png')
    
    
    
    #para verificar si un usuario es administrador o no(Para entrar en el admin)
    @property
    def is_staff(self):
         # "Is the user a member of staff?"
         if self.activo:
            return self.admin
         return False
     

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        
        super(Usuarios, self).save(*args, **kwargs)
        
        
        
        print(self.id,"Guardamos al usuario : ", self.username)



    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuarios'
        
        permissions = [
            #(Lo que se guarda en bases de datos, lo que se ve al usuario)
            #Permisos para master y gerente
            #("permisoscompletos", "Permisoscompletos"),
            
            
            
            
            
            
        ]#Fin de los permisos




####################################################################################


##########################################################################


#Señales para los metodos

@receiver(pre_save,sender=Usuarios)
def ModificarFotoPerfil(sender,instance,**kwargs):


    try:

        print(sender)
        print("sender: ",sender.imagenPerfil)
        instancia_vieja = sender.objects.get(pk = instance.pk)
        print("\n\nnombre:",instance)
        print("id: ",instance.id)

        #Con estas variables haremos las comparaciones
        nombre_foto_perfil = str(instancia_vieja.imagenPerfil)
        lista_nombres = nombre_foto_perfil.split('/')

        #print("viejo sender: ",instancia_vieja.imagenPerfil)

        #print(" En string: ",nombre_foto_perfil.split('/'))
        #print(" En lista: ",lista_nombres)
        #print(" Cantidad En lista: ",len(lista_nombres))
        
        
        #Aqui es cuando la foto es la por defecto(del sistema)
        if len(lista_nombres) == 3:
            print("Entramos en 3")
            print(" Ultimo elemento En lista: ",lista_nombres[-1])
        elif len(lista_nombres) == 4:
            print("Entramos en 4")

            print(instancia_vieja.imagenPerfil)
            #print("con name: ",instancia_vieja.imagenPerfil.name)
            #print("con name: ",instance.imagenPerfil.name)

            if str(instancia_vieja.imagenPerfil.name) == str(instance.imagenPerfil.name):
                print("La imagen de perfil se mantiene") 
                #Con esto borramos archivos
                #os.remove(ruta)
            else:
                print("Imagen de perfil cambiada")
                ruta = os.path.join(settings.MEDIA_ROOT,instancia_vieja.imagenPerfil.name)
                os.remove(ruta)
                print(" Eliminamos la foto: ",lista_nombres[-1])

            #print(instancia_vieja.imagenPerfil.url)
            #rutaNone = os.path.join(settings.MEDIA_ROOT)
            
            #ruta2 = os.path.join(settings.MEDIA_ROOT,instance.username,'perfil',lista_nombres[-1])
            
            #print(" rutaNone: ",ruta)
            
            

            #Con esto se borra una carpeta completa
            #shutil.rmtree(ruta)
            
        



        #print("sender: ",instancia_vieja.imagenPerfil.url)

    except sender.DoesNotExist:
        
    
        print("imagen: ",instance)
        #print("imagen: ",instance.imagenPerfil.url)
        #print("imagen nombre: ",instance.imagenPerfil)

    ######
    """
        
    try:
        #Para borrar el directorio y todo lo que haya dentro
        ruta = os.path.join(settings.MEDIA_ROOT,'img','fondos',instance.imagen.name)
        print("imagen ruta: ",ruta)
        #Con esto borramos archivos
        os.remove(ruta)

        #Con esto borramos carpetas
        shutil.rmtree(ruta)
        print(ruta)

    except OSError as e:

        print(f"Error:{ e.strerror}")
         
    """
    ######
    #print(instance.imagen_fondo)
    print("ModificarFotoPerfil, SEÑAL MODIFICADORA")

    


##########################################################################################################
##########################################################################################################


