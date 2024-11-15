from django.shortcuts import render # Muestras las respuesta de los datos proporcionados por las vistas
from .models import Topic

def index(request):
    """La pagina de inicio para Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Muestra todos los temas."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
