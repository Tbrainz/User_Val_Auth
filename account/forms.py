from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class RegUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegUser, self).__init__(*args, **kwargs)
        for input in self.visible_fields():
            input.field.widget.attrs['class'] ='form-control'
            input.field.widget.attrs['placeholder'] = f'Enter {input.field.label}'