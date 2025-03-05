"""Define patrones de URL para accounts"""

from django.urls import path, include

app_name= 'accounts'
urlpatterns = [
    # Incluye url de autenticacion predeterminadas.
    path('', include('django.contrib.auth.urls')),
]