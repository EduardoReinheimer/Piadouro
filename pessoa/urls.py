from django.urls import path
from pessoa.views import Home, UsersList, Follow, RedirectHome, Registration, ProfileEditor

urlpatterns = [
    path('', RedirectHome.as_view(), name='home'),
    path('cadastro/', Registration.as_view(), name='registration'),
    path('editor-perfil/', ProfileEditor.as_view(), name='profile-editor'),
    path('usuarios/', UsersList.as_view(), name='usuarios'),
    path('follow/<int:profile_id>', Follow.as_view(), name='follow'),
    path('<username>/', Home.as_view(), name='perfil'),
]