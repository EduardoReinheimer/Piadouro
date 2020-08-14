from django.forms import ModelForm, inlineformset_factory
from django.contrib.auth.models import User 
from pessoa.models import Perfil

class UserForm(ModelForm):

    class Meta:
        model = User
        exclude = ['is_staff', 'is_active', 'date_joined', 'last_login']


class ProfileForm(ModelForm):

    class Meta:
        model = Perfil
        exclude = ['usuario']

UserProfileForm = inlineformset_factory(User, Perfil, exclude=('usuario',))