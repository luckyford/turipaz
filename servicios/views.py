from django.shortcuts import render, get_object_or_404
from .models import Servicio

def lista_servicios(request):
    # Crear servicios de ejemplo si no existen
    if Servicio.objects.count() == 0:
        Servicio.objects.create(
            nombre="H. Ayuntamiento de Los Reyes La Paz",
            categoria="gobierno",
            descripcion="Oficina principal del gobierno municipal donde se realizan trámites y servicios ciudadanos.",
            direccion="Av. Puebla, Centro, Los Reyes La Paz, Estado de México",
            telefono="No disponible",
            email="No disponible",
            precio_rango="Gratuito"
        )

        Servicio.objects.create(
            nombre="Registro Civil La Paz",
            categoria="gobierno",
            descripcion="Oficialía del Registro Civil para actas de nacimiento, matrimonio y defunción.",
            direccion="Centro de Los Reyes La Paz, Estado de México",
            telefono="No disponible",
            email="No disponible",
            precio_rango="Variable"
        )

        Servicio.objects.create(
            nombre="IMSS Subdelegación Los Reyes La Paz",
            categoria="salud",
            descripcion="Servicios médicos, afiliación y atención del Instituto Mexicano del Seguro Social.",
            direccion="Los Reyes La Paz, Estado de México",
            telefono="800 623 2323",
            email="No disponible",
            precio_rango="Según afiliación"
        )

        Servicio.objects.create(
            nombre="DIF Municipal La Paz",
            categoria="social",
            descripcion="Apoyo social, psicológico y programas de asistencia para familias.",
            direccion="Los Reyes La Paz, Estado de México",
            telefono="No disponible",
            email="No disponible",
            precio_rango="Gratuito"
        )

        Servicio.objects.create(
            nombre="OPDAPAS La Paz",
            categoria="servicios públicos",
            descripcion="Organismo encargado del agua potable, drenaje y saneamiento.",
            direccion="Los Reyes La Paz, Estado de México",
            telefono="No disponible",
            email="No disponible",
            precio_rango="Variable"
        )

        Servicio.objects.create(
            nombre="Metro Los Reyes",
            categoria="transporte",
            descripcion="Estación del metro que conecta Los Reyes La Paz con la Ciudad de México.",
            direccion="Los Reyes La Paz, Estado de México",
            telefono="No disponible",
            email="No disponible",
            precio_rango="$5 MXN"
        )

        Servicio.objects.create(
            nombre="Correos de México - Los Reyes",
            categoria="paqueteria",
            descripcion="Servicio postal para envío de cartas y paquetes nacionales.",
            direccion="Los Reyes Acaquilpan, Estado de México",
            telefono="800 701 7000",
            email="No disponible",
            precio_rango="Variable"
        )

        Servicio.objects.create(
            nombre="Estafeta Los Reyes La Paz",
            categoria="paqueteria",
            descripcion="Servicio de mensajería y paquetería nacional e internacional.",
            direccion="Los Reyes La Paz, Estado de México",
            telefono="800 378 2338",
            email="clientes@estafeta.com",
            precio_rango="Variable"
        )

        Servicio.objects.create(
            nombre="Gasolinera Servicio Graciel",
            categoria="energia",
            descripcion="Estación de servicio para carga de combustible.",
            direccion="Los Reyes La Paz, Estado de México",
            telefono="No disponible",
            email="No disponible",
            precio_rango="Según combustible"
        )

    servicios = Servicio.objects.all()
    return render(request, 'servicios/lista_servicios.html', {'servicios': servicios})

def detalle_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    return render(request, 'servicios/detalle_servicio.html', {'servicio': servicio})
