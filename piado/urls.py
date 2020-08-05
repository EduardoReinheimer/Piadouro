from django.urls import path
from piado.views import PiadoCreate

urlpatterns = [
    path('adicionar', PiadoCreate.as_view(), name='piado-create'),
]
