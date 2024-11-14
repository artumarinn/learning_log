"""Define patrones de urls para learning logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Pagina de inicio
    path('', views.index, name='index'),
]