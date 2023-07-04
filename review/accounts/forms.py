from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = EmailField(required=True, label="メールアドレス")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

