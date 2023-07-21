
import os
import shutil #libreria para borrar carpetas esten o no llenas
from django.conf import settings

#Modelos creados para las jugadas
from aplicaciones.usuarios.models import Usuarios

#Estos dos modelos son para crear permisos personalizados
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType



#Aqui realizaremos todos los signal para los usuarios

def BorrarTipo_Jugada(sender,instance,**kwargs):

    print(sender)
    print(instance)
    print("Tipo de jugada fuera de los modelos: ",instance.nombre)

    #content_type = ContentType.objects.get_for_model(sender)
    #Permiso_Personalizado = Permission.objects.filter(name=str(instance.nombre),content_type=content_type)
    Permiso_Personalizado = Permission.objects.filter(name=str(instance.nombre))
    print("Permiso actual: ",Permiso_Personalizado)

    if Permiso_Personalizado.count()>0:
        Permiso_Personalizado = Permission.objects.get(name=instance.nombre)
        Permiso_Personalizado.delete()
        print("Se acaba de Borrar un permiso personalizado")
    else:
        pass
        print("No hay nada que borrar")


"""
def BorrarTipo_Jugada(sender,instance,**kwargs):

    print(sender)
    print(instance)
    print("Tipo de jugada fuera de los modelos: ",instance.nombre)

    
    try:
        #Para borrar la categoria de "descargas" y las demas categorias y todo lo que haya dentro
        if instance.nombre == "descargas":
            ruta = os.path.join(settings.MEDIA_ROOT,instance.nombre)
            videos = TipoJugadas.objects.filter(categoria=instance.id) #Aqui borramos todos los videos de esta categoria
            videos.delete()

        else:

            ruta = os.path.join(settings.MEDIA_ROOT)+"/videos/"+instance.nombre
            videos = Video.objects.filter(categoria=instance.id) #Aqui borramos todos los videos de esta categoria
            videos.delete()
            
        shutil.rmtree(ruta)

        Permiso = Permission.objects.get(name="ver_"+instance.nombre)
        Permiso.delete()

        print(ruta)

    except OSError as e:
        print(f"Error:{ e.strerror}")

    


    print("Se acaba de Borrar una Categoria jajaja")
"""


def ActualizarRepetidor_Jugada(sender,instance,**kwargs):
    pass

"""
    print(sender)
    print(instance)
    print("jugada: ",instance.id_jugada.digitos)
    elemento = Jugada.objects.get(id=instance.id_jugada.id)
    elemento.repetidor -=1
    elemento.save()

    print("Elemento id: ",elemento.id)
    print("Elemento digitos: ",elemento.digitos)

    #content_type = ContentType.objects.get_for_model(sender)
    #Permiso_Personalizado = Permission.objects.filter(name=str(instance.nombre),content_type=content_type)
"""
