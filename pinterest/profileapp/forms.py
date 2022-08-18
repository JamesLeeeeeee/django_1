from profileapp.models import Profile

from django.forms import ModelForm


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        field = ['image', 'nickname', 'message']
