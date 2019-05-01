from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from .models import *
from django.contrib.auth.models import User

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.emailconfirm.email_confirmed)
        )
account_activation_token = TokenGenerator()
