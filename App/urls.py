from django.urls import path, include
from App import views
#app_name= 'App'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('productos/', views.productos, name='productos'),
    path('locales/', views.locales, name='locales'),
    path('usuariosformulario', views.UsuariosFormulario, name='UsuariosFormularios'),
    path('BusquedaUsuarios', views.BusquedaUsuarios, name='busquedausuarios'),
    path('Buscar/', views.Buscar, name='buscar'),
    path('comprasformulario', views.ComprasFormulario, name='ComprasFormularios'),
    path('BusquedaCompras', views.BusquedaCompras, name='busquedacompras'),
    path('BuscarC/', views.BuscarC, name='buscarc'),
    path('productosformulario', views.ProductosFormulario, name='productosformulario'),
    path('BusquedaProductos', views.BusquedaProductos, name='busquedaproductos'),
    path('BuscarP/', views.BuscarP, name= 'buscarp'),

]