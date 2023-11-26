from django.contrib import admin
from django.urls import path
from aplicacion import views as app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', app.iniciar_sesion,name="login"),
    path('logout/', app.cerrar_sesion, name='logout'),
    path('',app.index,name="home"),
    path('registro/',app.reg_user,name="register"),
    path('proveedores/', app.proveedoresList, name='proveedores-list'),
    path('proveedores/agregar/', app.agregarProveedor, name='agregar-proveedor'),
    path('productos/',app.productosList)
]