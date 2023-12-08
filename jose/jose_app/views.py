from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm
from django.urls import reverse

def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/listar_reservas.html', {'reservas': reservas})

def agregar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/agregar_reserva.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Reserva
from django.contrib import messages

def modificar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)

    if request.method == 'POST':
        try:
            # Recupera los datos del formulario
            nombre = request.POST.get('nombre')
            telefono = request.POST.get('telefono')
            fecha = request.POST.get('fecha')
            hora = request.POST.get('hora')
            cantidad_personas = request.POST.get('cantidad_personas')
            correo = request.POST.get('correo')
            estado = request.POST.get('estado')
            observacion = request.POST.get('observacion')

            # Actualiza los campos del objeto reserva con los nuevos datos
            reserva.nombre = nombre
            reserva.telefono = telefono
            reserva.fecha = fecha
            reserva.hora = hora
            reserva.cantidad_personas = cantidad_personas
            reserva.correo = correo
            reserva.estado = estado
            reserva.observacion = observacion

            # Guarda los cambios en la base de datos
            reserva.save()

            # Mensaje de éxito
            messages.success(request, 'Reserva modificada con éxito.')

            # Redirige a la lista de reservas
            return redirect(reverse('listar_reservas'))
        except ValueError as e:
            # Imprime el error para entender qué valor causó el problema
            print('Error:', e)
            messages.error(request, 'Error al procesar el formulario. Inténtalo de nuevo.')
            return render(request, 'modificar_reserva.html', {'reserva': reserva})
    else:
        # Si el método no es POST, renderiza el formulario para editar la reserva
        return render(request, 'modificar_reserva.html', {'reserva': reserva})


def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)

    if request.method == 'POST':
        reserva.delete()
        return redirect('listar_reservas')

    return render(request, 'reservas/eliminar_reserva.html', {'reserva': reserva})
