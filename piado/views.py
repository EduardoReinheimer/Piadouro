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
        form.instance.proprietario = self.request.user
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('home'))

    def get_success_url(self):
        return reverse('home')


class PiadoDelete(LoginRequiredMixin, DeleteView):
    model = Piado
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return self.post(self, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.proprietario != request.request.user:
            raise PermissionDenied()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class PiadoLike(LoginRequiredMixin, UpdateView):
    model = Piado

    def get(self, request, *args, **kwargs):
        success_url = reverse('perfil', args=[request.GET['next_user']])
        self.object = self.get_object()
        if self.object.curtidas.filter(id=request.user.id).exists():
            self.object.curtidas.remove(request.user.id)
        else:
            self.object.curtidas.add(request.user.id)

        return HttpResponseRedirect(success_url)


class RePiado(LoginRequiredMixin, CreateView):
    model = Piado

    def get(self, request, *args, **kwargs):
        next_user = request.GET.get('next_user')

        if next_user:
            success_url = reverse('perfil', args=[next_user])
        else:
            success_url = reverse('home')

        repiado_query = Piado.objects.filter(proprietario=request.user, repiado_hospedeiro_id=kwargs['pk'])

        if repiado_query.exists():
            repiado_query.delete()
        else:
            piado_velho = get_object_or_404(Piado, id=kwargs['pk'])
            novo_piado = Piado(
                proprietario=request.user,
                conteudo=piado_velho.conteudo,
                repiado_hospedeiro=piado_velho
            )
            novo_piado.save()
        return HttpResponseRedirect(success_url)


class PiadoView(LoginRequiredMixin, DetailView):
    model = Piado
    template_name = 'piado/detail.html'


class PiadoComment(LoginRequiredMixin, CreateView):
    model = Piado
    fields = ['conteudo']

    def form_valid(self, form):
        comentario_hospedeiro = get_object_or_404(
            Piado, id=self.kwargs['hospedeiro'])
        form.instance.comentario_hospedeiro = comentario_hospedeiro
        form.instance.proprietario = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(self.request.GET.get('next_page_on_error', '/'))

    def get_success_url(self):
        return reverse('piado-detail', args=[self.kwargs['hospedeiro']])
