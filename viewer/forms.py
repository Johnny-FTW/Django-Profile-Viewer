
from django.contrib.auth.forms import UserCreationForm, get_user_model


class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')