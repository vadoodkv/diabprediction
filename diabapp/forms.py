from django.forms import ModelForm
from .models import signupmod

class signupForm(ModelForm):
    class Meta:
        model=signupmod