from django.shortcuts import render, redirect # Muestras las respuesta de los datos proporcionados por las vistas
from .models import Topic
from .forms import TopicForm

def index(request):
    """La pagina de inicio para Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Muestra todos los temas."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Muestra un tema concreto y todas sus entradas"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Añade un tema nuevo"""
    if request.method != 'POST':
        # No se ha enviado datos; crea un formulario en blanco.
        form = TopicForm()
    else:
        # Datos POST enviados; procesa datos.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs/new_topic.html', context)
    
    # Muestra un formulario en blanco o no valido.
    context = {'form': form} 
    return render(request, 'learning_logs/new_topic.html', context)