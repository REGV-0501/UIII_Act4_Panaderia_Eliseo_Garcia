from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingrediente, Receta
from django.urls import reverse
from django.utils import timezone

def inicio_panaderia(request):
    # Página principal de la app
    # Obtener el año actual para el footer
    now = timezone.now()
    return render(request, 'inicio.html', {'now': now})

def agregar_ingrediente(request):
    if request.method == 'POST':
        # Si la solicitud es POST, procesar los datos del formulario
        nombre = request.POST.get('nombre', '').strip()
        descripcion = request.POST.get('descripcion', '').strip() or None
        unidad_medida = request.POST.get('unidad_medida', '').strip()
        costo_unitario = request.POST.get('costo_unitario')
        proveedor = request.POST.get('proveedor', '').strip() or None
        fecha_compra = request.POST.get('fecha_compra')
        stock_disponible = request.POST.get('stock_disponible')

        # Crear y guardar el ingrediente
        ingrediente = Ingrediente(
            nombre=nombre,
            descripcion=descripcion,
            unidad_medida=unidad_medida,
            costo_unitario=costo_unitario,
            proveedor=proveedor,
            fecha_compra=fecha_compra,
            stock_disponible=stock_disponible
        )
        ingrediente.save()
        
        # Después de guardar, redirigir a la vista de ver ingredientes
        return redirect('ver_ingredientes')
    else:
        # Si la solicitud es GET, simplemente mostrar el formulario vacío
        return render(request, 'ingredientes/agregar_ingrediente.html', {})

def ver_ingredientes(request):
    ingredientes = Ingrediente.objects.all().order_by('nombre')
    return render(request, 'ingredientes/ver_ingredientes.html', {'ingredientes': ingredientes})

def actualizar_ingrediente(request, ingrediente_id):
    ingrediente = get_object_or_404(Ingrediente, id=ingrediente_id)
    return render(request, 'ingredientes/actualizar_ingrediente.html', {'ingrediente': ingrediente})

def realizar_actualizacion_ingrediente(request, ingrediente_id):
    ingrediente = get_object_or_404(Ingrediente, id=ingrediente_id)
    if request.method == 'POST':
        ingrediente.nombre = request.POST.get('nombre', ingrediente.nombre).strip()
        ingrediente.descripcion = request.POST.get('descripcion', ingrediente.descripcion).strip() or None
        ingrediente.unidad_medida = request.POST.get('unidad_medida', ingrediente.unidad_medida).strip()
        ingrediente.costo_unitario = request.POST.get('costo_unitario', ingrediente.costo_unitario)
        ingrediente.proveedor = request.POST.get('proveedor', ingrediente.proveedor).strip() or None
        ingrediente.fecha_compra = request.POST.get('fecha_compra', ingrediente.fecha_compra)
        ingrediente.stock_disponible = request.POST.get('stock_disponible', ingrediente.stock_disponible)
        ingrediente.save()
        return redirect('ver_ingredientes')
    # Si se accede por GET, redirigir al formulario de edición
    return redirect('actualizar_ingrediente', ingrediente_id=ingrediente.id)

def borrar_ingrediente(request, ingrediente_id):
    ingrediente = get_object_or_404(Ingrediente, id=ingrediente_id)
    if request.method == 'POST':
        ingrediente.delete()
        return redirect('ver_ingredientes')
    return render(request, 'ingredientes/borrar_ingrediente.html', {'ingrediente': ingrediente})
def agregar_receta(request):
    ingredientes_disponibles = Ingrediente.objects.all().order_by('nombre')
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        descripcion = request.POST.get('descripcion', '').strip() or None
        tiempo_preparacion = request.POST.get('tiempo_preparacion')
        fecha_creacion = request.POST.get('fecha_creacion')
        autor = request.POST.get('autor', '').strip()

        receta = Receta(
            nombre=nombre,
            descripcion=descripcion,
            tiempo_preparacion=tiempo_preparacion,
            fecha_creacion=fecha_creacion,
            autor=autor
        )
        receta.save()

        # Manejar ingredientes many-to-many
        ingredientes_seleccionados_ids = request.POST.getlist('ingredientes')
        receta.ingredientes.set(ingredientes_seleccionados_ids)

        return redirect('ver_recetas')
    return render(request, 'recetas/agregar_receta.html', {'ingredientes_disponibles': ingredientes_disponibles})

def ver_recetas(request):
    recetas = Receta.objects.all().order_by('nombre')
    return render(request, 'recetas/ver_recetas.html', {'recetas': recetas})

def actualizar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    ingredientes_disponibles = Ingrediente.objects.all().order_by('nombre')
    ingredientes_seleccionados = receta.ingredientes.all() # Obtener los ingredientes ya asociados a la receta

    context = {
        'receta': receta,
        'ingredientes_disponibles': ingredientes_disponibles,
        'ingredientes_seleccionados': ingredientes_seleccionados,
    }
    return render(request, 'recetas/actualizar_receta.html', context)

def realizar_actualizacion_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.method == 'POST':
        receta.nombre = request.POST.get('nombre', receta.nombre).strip()
        receta.descripcion = request.POST.get('descripcion', receta.descripcion).strip() or None
        receta.tiempo_preparacion = request.POST.get('tiempo_preparacion', receta.tiempo_preparacion)
        receta.fecha_creacion = request.POST.get('fecha_creacion', receta.fecha_creacion)
        receta.autor = request.POST.get('autor', receta.autor).strip()
        receta.save()

        # Actualizar ingredientes many-to-many
        ingredientes_seleccionados_ids = request.POST.getlist('ingredientes')
        receta.ingredientes.set(ingredientes_seleccionados_ids)

        return redirect('ver_recetas')
    return redirect('actualizar_receta', receta_id=receta.id)

def borrar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.method == 'POST':
        receta.delete()
        return redirect('ver_recetas')
    return render(request, 'recetas/borrar_receta.html', {'receta': receta})