from django.urls import path
from piado.views import PiadoCreate, PiadoDelete

urlpatterns = [
    path('adicionar/', PiadoCreate.as_view(), name='piado-create'),
    path('remover/<int:pk>/', PiadoDelete.as_view(), name='piado-delete'),
]
