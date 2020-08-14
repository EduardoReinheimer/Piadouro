from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from pessoa.models import Perfil
from django.contrib.auth.mixins import LoginRequiredMixin
from pessoa.forms import UserForm, UserProfileForm


class Home(DetailView):
    template_name = 'home.html'
    model = User

    def get_object(self):
        return get_object_or_404(self.model, username=self.kwargs['username'])

class UsersList(ListView):
    template_name= 'user_list.html'
    model = Perfil

class Follow(RedirectView):
    permanent = False
    query_string= False 
    pattern_name = 'usuarios'

    def get_redirect_url(self, *args, **kwargs):
        profile_to_follow = get_object_or_404(Perfil, pk=kwargs['profile_id'])
        if self.request.user.perfil.seguindo.filter(pk=profile_to_follow.pk).exists():
            self.request.user.perfil.seguindo.remove(profile_to_follow)
        else:
            self.request.user.perfil.seguindo.add(profile_to_follow)
        return super().get_redirect_url()

class RedirectHome(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = False
    pattern_name = 'perfil'

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(self.request.user.username)
        
class Registration(CreateView):
    model = User
    template_name = 'create_user.html'
    form_class = UserForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profile_form'] = UserProfileForm()
        return context