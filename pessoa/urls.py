from django.urls import path
from pessoa.views import Home, UsersList

urlpatterns = [
    path('usuarios/', UsersList.as_view(), name='usuarios'),
    path('<username>/', Home.as_view(), name='perfil'),
]