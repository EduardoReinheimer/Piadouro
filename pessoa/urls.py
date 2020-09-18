from django.urls import path
from pessoa.views import Home, UsersList, Follow, Registration, ProfileEditor, UserDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cadastro/', Registration.as_view(), name='registration'),
    path('editor-perfil/', ProfileEditor.as_view(), name='profile-editor'),
    path('usuarios/', UsersList.as_view(), name='usuarios'),
    path('seguir/<int:user_id>', Follow.as_view(), name='follow'),
    path('<str:username>/', UserDetail.as_view(), name='perfil')
]