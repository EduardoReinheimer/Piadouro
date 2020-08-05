from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class Home(DetailView):
    template_name = 'home.html'
    model = User

    def get_object(self):
        return get_object_or_404(self.model, username=self.kwargs['username'])

class UsersList(ListView):
    template_name= 'user_list.html'
    model = User

    
