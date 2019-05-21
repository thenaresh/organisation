from django.urls import path
from django.conf import settings
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView

from . import views

urlpatterns = [
    path('', views.index, name='index'),

]