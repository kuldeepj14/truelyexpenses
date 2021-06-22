from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type
import datetime

class AppTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, template):
        return (text_type(user.is_active) + text_type(user.pk) + text_type(datetime.datetime.now().timestamp()))

token_generator = AppTokenGenerator()