from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='Welcome'),
    # CRUD routes
    path('tienda/listado_productos', views.listado_productos, name='listado productos'),
    path('tienda/listado_productos/crear_marca', views.crear_marca, name='crear marca'),
    path('tienda/listado_productos/crear_producto', views.crear_producto, name='crear producto'),
    path('tienda/listado_productos/buscar', views.buscar, name='buscar'),
    path('tienda/listado_productos/editar_producto/<int:pk>', views.editar_producto, name='editar producto'),
    path('tienda/listado_productos/eliminar_producto/<int:pk>', views.eliminar_producto, name='eliminar producto'),
]
