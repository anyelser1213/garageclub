from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views as vistasBasePrincipal


app_name ="base_principal"

urlpatterns = [
    

    
    path('', vistasBasePrincipal.Index.as_view() ,name="index"),




    #Para las apis
    #path('probando/', views.Probando ,name="probando"),
    #path('api_login/', views.api_login ,name="api_login"),

    
    
    
] 