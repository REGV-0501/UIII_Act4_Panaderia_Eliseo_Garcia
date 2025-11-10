from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_panaderia, name='inicio_panaderia'),
    path('ingredientes/agregar/', views.agregar_ingrediente, name='agregar_ingrediente'),
    path('ingredientes/', views.ver_ingredientes, name='ver_ingredientes'),
    path('ingredientes/editar/<int:ingrediente_id>/', views.actualizar_ingrediente, name='actualizar_ingrediente'),
    path('ingredientes/editar/guardar/<int:ingrediente_id>/', views.realizar_actualizacion_ingrediente, name='realizar_actualizacion_ingrediente'),
    path('ingredientes/borrar/<int:ingrediente_id>/', views.borrar_ingrediente, name='borrar_ingrediente'),

    path('recetas/agregar/', views.agregar_receta, name='agregar_receta'),
    path('recetas/', views.ver_recetas, name='ver_recetas'),
    path('recetas/editar/<int:receta_id>/', views.actualizar_receta, name='actualizar_receta'),
    path('recetas/editar/guardar/<int:receta_id>/', views.realizar_actualizacion_receta, name='realizar_actualizacion_receta'),
    path('recetas/borrar/<int:receta_id>/', views.borrar_receta, name='borrar_receta'),
]