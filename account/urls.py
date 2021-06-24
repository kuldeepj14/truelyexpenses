from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.index, name="account"),
    path('edit-details', views.edit_account_details, name="edit-account-details" ),
    path('password-reset/', views.password_reset, name="account-password-reset" )
]