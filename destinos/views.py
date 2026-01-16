from django.shortcuts import render, get_object_or_404, redirect
from .models import Destino
from usuarios.forms import ComentarioForm
from django.contrib.auth.decorators import login_required
from usuarios.models import Comentario

def lista_destinos(request):
    # Crear destinos de ejemplo si no existen
    if Destino.objects.count() == 0:
        Destino.objects.create(
            nombre="Unidad deportiva Soraya Jimenez",
            descripcion="La Unidad Deportiva Soraya Jiménez es un complejo deportivo ubicado en Los Reyes La Paz, Estado de México, que cuenta con diversas instalaciones para la práctica de deportes y actividades recreativas. Fue construido en honor a la medallista olímpica Soraya Jiménez, con el objetivo de fomentar el deporte y alejar a los jóvenes de la delincuencia.",
            ubicacion=" Alberca semiolímpica techada, Canchas de futbol soccer profesional y futbol rápido, Canchas de básquetbol, Pista de atletismo de tartán, Gimnasio, Áreas de ejercitadores y módulos de juegos infantiles, Áreas verdes y asadores",
            tipo="natural",
            horario="Lunes a viernes: 07:00 - 18:00 horas, Sábado y domingo: 07:00 - 18:00 horas",
            precio_aprox=00.00
        )
        Destino.objects.create(
            nombre="CLUB DEPORTIVO AEROGYM",
            descripcion="El Club Deportivo Aerogym es un gimnasio en Los Reyes La Paz, Estado de México, que ofrece diversas actividades como pesas, CrossFit, natación, zumba, box, karate, danzas y kickboxing, destacando por su variedad y trayectoria de 37 años, con contacto vía redes sociales (Facebook, Instagram) o números de teléfono para más información.",
            ubicacion="Calle 9 Esquina Avenida Lerma, Los Reyes, La Paz, Estado de México.",
            tipo="natural",
            horario="Lunes 5:00 - 22:00,Martes 5:00 - 22:00,Miércoles 5:00 - 22:00,Jueves 5:00 - 22:00,Viernes 5:00 - 22:00,Sábado 6:00 - 15:00,Domingo 8:00 - 16:00",   
            precio_aprox=300.00
        )
        Destino.objects.create(
            nombre="Club deportivo la paz",
            descripcion="El club deportivo la paz es un parque se encuentra ubicado en Isidro 7, Los Reyes, 56400 Los Reyes Acaquilpan, Méx. Cuenta con diversas atracciones y juegos donde se podrá pasar el rato en familia cuenta con diversas áreas verdes.",
            ubicacion="Isidro 7, Los Reyes, 56400 Los Reyes Acaquilpan, Méx.",
            tipo="deportivo",
            horario="Domingo Cerrado,Lunes 7 a.m.–8:30 p.m.,Martes 7 a.m.–8:30 p.m.,Miércoles 7 a.m.–8:30 p.m.,Jueves 7 a.m.–8:30 p.m.,Viernes 7 a.m.–8:30 p.m.,Sábado 7 a.m.–2 p.m.",
            precio_aprox=00.00  
        )
        Destino.objects.create(
            nombre="Parque Francisco villa",
            descripcion="El Parque Francisco Villa en Los Reyes La Paz, Estado de México, es un espacio recreativo familiar con juegos infantiles, áreas verdes, canchas y un foro, que a menudo es sede de eventos comunitarios y ferias locales, funcionando como un importante pulmón verde en la zona y ofreciendo actividades gratuitas y servicios de salud temporal, siendo un punto de encuentro para familias y residentes en el municipio de La Paz.",
            ubicacion="Av. Puebla Manzana 006, Los Reyes, 56400 Los Reyes Acaquilpan, Méx.",
            tipo="areas recreativas",
            horario="Abierto las 24 horas",
            precio_aprox=30.00
        )
        Destino.objects.create(
            nombre="El Antiguo Templo de Los Reyes Acaquilpan en La Paz, Estado de México",
            descripcion="Es una zona arqueológica que conserva un basamento piramidal con tres etapas constructivas del Posclásico (1100-1521 d.C.), destacando por su orientación al poniente, inusual para templos dedicados a Huitzilopochtli, y restos de áreas habitacionales para gobernantes y sacerdotes, siendo un importante sitio subordinado a los Acolhuas y luego a los Mexicas, a pesar de estar rodeado por la urbanización actual.Características Principales:Estructura: Un basamento escalonado con una pirámide de tres cuerpos, construida en distintas fases del Posclásico (Mazapa, Tolteca-Chichimeca, Azteca).,Orientación: Orientada hacia el poniente, sugiriendo un culto a Huitzilopochtli, dios solar asociado al colibrí zurdo.,Contexto Histórico: Fue parte de un asentamiento prehispánico que estuvo bajo influencia de Tula y luego de los Acolhuas, con una fase tardía Mexica.,Restos Adicionales: Se encuentran vestigios de habitaciones adyacentes al basamento principal, que servían como morada de gobernantes y sacerdotes.",
            ubicacion="En el municipio de Los Reyes Acaquilpan, Estado de México, accesible por la carretera México-Texcoco, tomando la calle Prolongación Benito Juárez.",
            tipo="parque",
            horario="abierto de Lunes a Domingo",
            precio_aprox=00.00
        )
        Destino.objects.create(
            nombre="Copacabana",
            descripcion="Ciudad a orillas del Lago Titicaca, con la Basílica de Copacabana.",
            ubicacion="Lago Titicaca",
            tipo="cultural",
            horario="Todo el día",
            precio_aprox=60.00
        )
        Destino.objects.create(
            nombre="Isla del Sol",
            descripcion="Isla sagrada en el Lago Titicaca, con ruinas y paisajes andinos.",
            ubicacion="Lago Titicaca",
            tipo="historico",
            horario="Todo el día",
            precio_aprox=80.00
        )
        Destino.objects.create(
            nombre="Samaipata",
            descripcion="Sitio arqueológico preincaico con un monolito tallado en la roca.",
            ubicacion="Provincia Florida, Santa Cruz",
            tipo="historico",
            horario="9:00 - 17:00",
            precio_aprox=55.00
        )

    destinos = Destino.objects.all()
    return render(request, 'destinos/lista.html', {'destinos': destinos})

@login_required
def detalle_destino(request, destino_id):
    destino = get_object_or_404(Destino, _id=destino_id) # Use _id to get the Destino
    comentarios = Comentario.objects.filter(destino=destino) # Keep this filter
    # ... rest of the view ...
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.destino = destino
            comentario.save()
            return redirect('detalle_destino', destino_id=destino_id)
    else:
        form = ComentarioForm()

    return render(request, 'destinos/detalle.html', {
        'destino': destino,
        'comentarios': comentarios,
        'form': form
    })