from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplicaciones.usuarios'


    def ready(self):
        from django.contrib.auth.models import User
        from aplicaciones.usuarios.models import Usuarios
        from .funciones_receptoras import BorrarTipo_Jugada,ActualizarRepetidor_Jugada

        #Esta señal es cuando borremos un tipo de jugada
        #pre_delete.connect(BorrarTipo_Jugada, sender=TipoJugadas)

        #Esta señal es cuando borramos una jugada del dia(debe borrarse en la tabla de hoy y la dinamica del dia actual)

        #Esta señal es cuando borremos una jugada
        #pre_delete.connect(ActualizarRepetidor_Jugada, sender=Jugadas_Del_Dia)
