from django.shortcuts import render # Muestras las respuesta de los datos proporcionados por las vistas

def index(request):
    """La pagina de inicio para Learning Log."""
    return render(request, 'learning_logs/index.html')