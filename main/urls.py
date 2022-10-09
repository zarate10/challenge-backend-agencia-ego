from django.urls import path
from . import views 

urlpatterns = [
    path('', views.modelos, name="modelos"),
    path('login/', views.loguear, name="login"),
    path('desloguear/', views.desloguear, name="desloguear"), 
    path('car/add/', views.add_car, name="add_car"), 
    path('car/<int:id_veh>/edit', views.edit_car, name="edit_car"), 
    path('car/<int:id_veh>/delete', views.delete_car, name="delete_car"), 
    path('categoria/<int:id>/', views.filtro_autos, name="filtro_autos"),
    path('ficha/<str:name_car>', views.ficha_modelo, name="ficha"),
    # path('api/caracteristicas', views.caracteristicas, name="caracteristicas"),
    
    path('categoria/<int:id>/menor_precio', views.menor_precio_x_categoria, name="menor_precio_x_categoria"),
    path('menor_precio', views.menor_precio, name="menor_precio"),

    path('categoria/<int:id>/mayor_precio', views.mayor_precio_x_categoria, name="mayor_precio_x_categoria"),
    path('mayor_precio', views.mayor_precio, name="mayor_precio"),

    path('categoria/<int:id>/mas_viejo', views.mas_viejo_x_categoria, name="mas_viejo_x_categoria"),
    path('mas_viejo', views.mas_viejo, name="mas_viejo"),
    
    path('categoria/<int:id>/mas_nuevo', views.mas_nuevo_x_categoria, name="mas_nuevo_x_categoria"),
    path('mas_nuevo', views.mas_nuevo, name="mas_nuevo"),
]