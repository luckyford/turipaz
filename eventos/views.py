from django.shortcuts import render, get_object_or_404
from .models import Evento
from django.utils import timezone
import datetime

def lista_eventos(request):
    # Crear eventos de ejemplo si no existen
    if Evento.objects.count() == 0:
        Evento.objects.create(
            nombre="Casa de la cultura los reyes la paz",
            descripcion="La Casa de la Cultura de Los Reyes La Paz es un centro cultural que ofrece una amplia variedad de talleres artísticos y recreativos para todas las edades, como danza, música, artes plásticas y teatro, impartidos por instructores locales y personal municipal, funcionando como un espacio clave para la expresión y desarrollo cultural en el municipio, y puedes encontrar detalles de horarios y cursos en su página oficial o redes sociales.",
            fecha_inicio=datetime.date(2024, 1, 16),  # Ejemplo: 16 de enero de 2026
            fecha_fin=datetime.date(2024, 1, 16),  # Ejemplo: 16 de enero de 2026
            lugar="Av. Puebla, Los Reyes, 56400 Los Reyes Acaquilpan, Méx.",
            organizador="Personal municipal",
            costo="Variable (depende del taller)"
        )
        Evento.objects.create(
            nombre="Museo de los reyes la paz",
            descripcion="El Museo de los Reyes La Paz se refiere principalmente a la Zona Arqueológica Los Reyes La Paz, un sitio prehispánico en el Estado de México con una pirámide de tres cuerpos, orientada al poniente y asociada a Huitzilopochtli, además de otros atractivos históricos como la Parroquia del Divino Salvador y festividades locales.",
            fecha_inicio=datetime.date(2024, 1, 16),  # Ejemplo: 16 de enero de 2026
            fecha_fin=datetime.date(2024, 1, 16),  # Ejemplo: 16 de enero de 2026
            lugar="C. Benito Juárez S/N, Ampliación, 56400 Emiliano Zapata, Méx.",
            organizador="INAH",
            costo="Gratuito"
        )
        Evento.objects.create(
            nombre="Parroquia del divino salvador",
            descripcion="La Parroquia del Divino Salvador en Los Reyes La Paz (Tecamachalco) es un templo histórico del siglo XVIII, parte del patrimonio cultural de la zona, conocido por su arquitectura colonial y pinturas murales, y celebra su fiesta patronal el 6 de agosto, siendo un punto clave para la fe y la historia local",
            fecha_inicio=datetime.date(2024, 8, 6),  # Ejemplo: 6 de agosto de 2024
            fecha_fin=datetime.date(2024, 8, 6),  # Ejemplo: 6 de agosto de 2024
            lugar="Av. José María Morelos 1, Tecamachalco, 56500 Tecamachalco, Méx.",
            organizador="Arquidiócesis de Nezahualcóyotl",
            costo="Gratuito"
        )
        Evento.objects.create(
            nombre="Salónes de Eventos los reyes la paz",
            descripcion="En Los Reyes La Paz hay muchos salones para eventos, como Salón Los Reyes (paquetes de verano, 40 personas, $612 104 2373), Lalokura (paquetes desde $5,500, cerca del metro, 55 4554 8496), Jardín Los Reyes (bodas, jardín, capilla, 55 1660 7340), Real El Pino (desde $5900 para 100 personas, a 5 min del metro, 55 5960 4765), y El Edén (paquetes con/sin alimentos, Calle Río Champoton, 55 1660 7340).",
            fecha_inicio=datetime.date(2024, 1, 16),  # Ejemplo: 16 de enero de 2026
            fecha_fin=datetime.date(2024, 1, 16),  # Ejemplo: 16 de enero de 2026
            lugar="Los Reyes La Paz, Méx.",
            organizador="Diversos particulares",
            costo="Variable (depende del salón y el paquete)"
        )

    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'eventos/detalle_evento.html', {'evento': evento})