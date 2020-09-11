from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from pessoa.models import Perfil
from django.contrib.auth.mixins import LoginRequiredMixin
from pessoa.forms import UserForm, UserProfileForm, UserEditorForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from piado.models import Piado
from django.db.models import Q


class Home(DetailView):
    template_name = 'home.html'
    model = User

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['piados'] = Piado.objects.filter(proprietario=self.object) 
        return context

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
        user_to_follow = get_object_or_404(User, pk=kwargs['user_id'])
        if self.request.user.perfil.seguindo.filter(pk=user_to_follow.pk).exists():
            self.request.user.perfil.seguindo.remove(user_to_follow)
        else:
            self.request.user.perfil.seguindo.add(user_to_follow)
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
        context = {
            'action': reverse('registration'),
            'button_text': 'Cadastrar',
        }
        context['form'] = self.get_form()

        if self.request.method == 'POST':
            context['profile_form'] = UserProfileForm(self.request.POST, self.request.FILES)
        else:
            context['profile_form'] = UserProfileForm()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        if context['form'].is_valid() and context['profile_form'].is_valid():
            user = context['form'].save()
            user.set_password(context['form'].cleaned_data['password'])
            user.save()
            context['profile_form'].instance.usuario = user
            context['profile_form'].save()

            new_user = authenticate(
                request,
                username=context['form'].cleaned_data['username'],
                password=context['form'].cleaned_data['password'],
            )
            login(request, new_user)
            return redirect('home')
            
        return self.render_to_response(context)

class ProfileEditor(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'create_user.html'
    form_class = UserEditorForm

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, id=self.request.user.id)

    def get_context_data(self, *args, **kwargs):
        context = {
            'action': reverse('profile-editor'),
            'button_text': 'Atualizar',
        }
        self.object = self.get_object()
        context['form'] = self.get_form()

        if self.request.method == 'POST':
            context['profile_form'] = UserProfileForm(self.request.POST, self.request.FILES, instance=self.object.perfil)
        else:
            context['profile_form'] = UserProfileForm(instance=self.object.perfil)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        if context['form'].is_valid() and context['profile_form'].is_valid():
            user = context['form'].save()
            context['profile_form'].save()
            return redirect('home')
            
        return self.render_to_response(context)