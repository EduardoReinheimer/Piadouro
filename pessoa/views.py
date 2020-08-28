from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from pessoa.models import Perfil
from django.contrib.auth.mixins import LoginRequiredMixin
from pessoa.forms import UserForm, UserProfileForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


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
        context = {}
        context['form'] = self.get_form()

        if self.request.method == 'POST':
            context['profile_form'] = UserProfileForm(self.request.POST, self.request.FILES)
            print("é post")
        else:
            context['profile_form'] = UserProfileForm()
            print("deu ruim")
        print(context)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        print(context)
        print("post entrou")

        if context['form'].is_valid() and context['profile_form'].is_valid():
            print("form valido")
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