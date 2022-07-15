from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='index_login'), # funcao index
    path('login/',views.login, name='login'), # funcao de login
    path('logout/',views.logout, name='logout'), # funcao saida
    path('cadastro/',views.cadastro, name='cadastro'), # funcao de cadastro
    path('dashboard/',views.dashboard, name='dashboard'), # funcao principal
]