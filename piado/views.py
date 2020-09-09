from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from piado.models import Piado
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404


class PiadoCreate(LoginRequiredMixin, CreateView):
    model = Piado
    fields = ['conteudo']

    def form_valid(self, form):
        form.instance.usuario = self.request.user.perfil
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('perfil', args=[self.request.user.username])

class PiadoDelete(LoginRequiredMixin, DeleteView):
    model = Piado
    success_url = reverse_lazy('home')
    
    def get(self, request, *args, **kwargs):
        return self.post(self, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.usuario.id != request.request.user.id:
            raise PermissionDenied()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

class PiadoLike(LoginRequiredMixin, UpdateView):
    model = Piado

    def get(self, request, *args, **kwargs):
        success_url = reverse('perfil', args=[request.GET['next_user']])
        self.object = self.get_object()
        if self.object.curtidas.filter(id = request.user.perfil.id).exists():
            self.object.curtidas.remove(request.user.perfil.id)
        else: 
            self.object.curtidas.add(request.user.perfil.id)

        return HttpResponseRedirect(success_url)

class RePiado(LoginRequiredMixin, UpdateView):
    model = Piado

    def get(self, request, *args, **kwargs):
        success_url = reverse('perfil', args=[request.GET['next_user']])
        self.object = self.get_object()
        self
        if self.object.repiados.filter(id = request.user.perfil.id).exists():
            self.object.repiados.remove(request.user.perfil.id)
        elif self.object.usuario != request.user.perfil: 
            self.object.repiados.add(request.user.perfil.id)
        return HttpResponseRedirect(success_url)


class PiadoView(LoginRequiredMixin, DetailView):
    model = Piado
    template_name = 'piado/detail.html'
    
class PiadoComment(LoginRequiredMixin, CreateView):
    model = Piado
    fields = ['conteudo']

    def form_valid(self, form):
        piado_hospedeiro = get_object_or_404(Piado, id=self.kwargs['hospedeiro'])
        form.instance.piado_hospedeiro = piado_hospedeiro
        form.instance.usuario = self.request.user.perfil
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('piado-detail', args=[self.kwargs['hospedeiro']])
    