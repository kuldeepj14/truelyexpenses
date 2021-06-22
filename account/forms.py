from django import forms
from django.db.models import fields
from .models import UserAccount
from django.contrib.auth import get_user_model

User = get_user_model()

class PartialUserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = (
            "phone_number",
            'birth_date',
        )

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )