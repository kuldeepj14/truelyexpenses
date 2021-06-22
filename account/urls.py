from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.index, name="account"),
    # path('edit-account', views.edit_account, name="edit-account" ),
    path('password-reset/', views.password_reset, name="account-password-reset" )
]