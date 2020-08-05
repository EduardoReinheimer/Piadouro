from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from piado.models import Piado
from django.urls import reverse


class PiadoCreate(LoginRequiredMixin, CreateView):
    model = Piado
    fields = ['conteudo']

    def form_valid(self, form):
        form.instance.usuario = self.request.user.perfil
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('perfil', args=[self.request.user.username])
