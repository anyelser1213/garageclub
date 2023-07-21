from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from aplicaciones.usuarios.form import UsuarioPersonalizadoForm
from aplicaciones.ofertas.models import Contrato

#Clases para las plantillas
from django.views.generic import View,TemplateView, CreateView, UpdateView, DetailView, ListView, DeleteView

# Create your views here.

class Perfil_Usuario(TemplateView):

    template_name = "usuarios/perfil-usuario.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            return redirect("login:login")

        else:

            print("Estas autenticado GENIAL")
            #print("usuario permisos: ",request.user.get_all_permissions())
            #Aqui verificamos si el usuario esta activo para que ingrese
            ''' 
            if request.user.activo:   
                print("Usuario activo y validado")
            else:
                print("El usuario no esta activo")
                messages.add_message(request, messages.INFO, "Usuario Inactivo")
                return redirect("src:logout")
            '''


        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):


        context = super().get_context_data(**kwargs)
        #context['informacion'] = "Hola..."

       
        context['usuario'] = self.request.user
        #context['contrato'] = Contrato.objects.get(usuario=self.request.user)
        context['contrato'] = "Sin contrato"
        print("en contextos:",context['contrato'])
        return context

 

def registrarUsuarioPersonalizado(request):

    #verificamos que estamos logeados
    if request.user.is_authenticated:
        
        contexto = {}
        #Cuando solicitamos una pagina
        if request.method == "GET":
            
            print("ENTRAMOS EN GET PARA CREAR LA PETICION")
            form = UsuarioPersonalizadoForm(usuario=request.user)
            contexto = {'form': form,
                        'user': request.user}
            contexto['contrato'] ="SIN CONTRATO"

            contrato_usuario = Contrato.objects.filter(usuario=request.user)
            if contrato_usuario.exists():
                print("Si tiene contrato")
                
                #Verificamos si tiene el contrato vigente
                contrato_vigente = Contrato.objects.get(usuario=request.user)
                if contrato_vigente.estado_contrato == "vigente":
                    print("El contrato del usuario:",request.user.username,"SI esta vigente.")
                    #contexto['ofertas'] = Peticion.objects.filter(tipo_peticion="nacional")
                    contexto['contrato'] ="CONTRATO VIGENTE"

                else:
                    print("El contrato del usuario:",request.user.username,"NO esta vigente.")
                    #contexto['ofertas'] = Peticion.objects.none()
                    contexto['contrato'] ="CONTRATO CADUCADO"
            else:
                print("No tiene contrato")
                contexto['contrato'] ="SIN CONTRATO"
                #print("entramos en GET:", orden)






        #Metodo(POST)
        else:

            #print(request.POST)
            print("\nEntramos en POST de registrar usuario\n")
            print(request.POST)
            form = UsuarioPersonalizadoForm(data=request.POST,usuario=request.user)

            #Variables para guardar
            #productos = request.POST.getlist('productos')
            #calidad = request.POST.getlist('calidad')
            #cantidad = request.POST.getlist('cantidad')
            
            #print(productos," jajajajaja")

            #si el formulario tiene los datos correctos entramos aqui
            
            
            
            #En caso de que el formulario sera correcto
            if form.is_valid():
            # and trabajo.is_valid() and suministro.is_valid():
            
            
                print("\nEl formulario es correcto")





                return redirect('peticiones:PeticionListar')
                #print("entramos aqui en POST")
                #orden = form.save()
                #orden_creada = orden.save(commit=False)
                #print("ORDEN CREADA:",orden_creada)
                #print(orden_creada.id)
                #print(orden_creada.observacion)
                #orden_creada.save()
            
                #print(suministro.cleaned_data)

                
            #    contexto = {'user': request.user,
            #                }
                
            
            
            
            else:

                print("la orden no fue creada...")
                
            # redirect to a new URL:
            print("Probando aqui......")
            return render(request, 'usuarios/usuario-crear.html',contexto)
    
    
    
    
    #Si el usuario no esta autenticado
    else:

        print("USUARIO NO AUTENTICADO")
        return redirect('/login')


    #print(contexto)
    return render(request, 'usuarios/usuario-crear.html', contexto)
