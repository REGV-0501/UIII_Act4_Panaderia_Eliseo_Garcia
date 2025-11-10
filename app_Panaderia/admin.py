from django.contrib import admin
from .models import Ingrediente, Receta# Solo Ingrediente por ahora

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'unidad_medida', 'costo_unitario', 'proveedor', 'fecha_compra', 'stock_disponible')
    search_fields = ('nombre', 'proveedor')
    list_filter = ('unidad_medida', 'proveedor', 'fecha_compra')
    date_hierarchy = 'fecha_compra' # Para una navegación por fechas en el admin
    
@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tiempo_preparacion', 'autor', 'fecha_creacion')
    search_fields = ('nombre', 'autor')
    list_filter = ('autor', 'fecha_creacion')
    date_hierarchy = 'fecha_creacion'
    # Para poder seleccionar ingredientes en el admin
    filter_horizontal = ('ingredientes',) # Esto genera un widget más amigable para ManyToMany