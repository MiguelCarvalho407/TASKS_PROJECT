from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),

    # ========== REGISTRATION ========== #

    path('accounts/signup/', views.signup_view, name='signup'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ========== APP ========== #

    path('app/', views.app, name='app'),
    path('app/listatarefas', views.listatarefas, name='listatarefas'),
    path('app/criartarefa/', views.criartarefa, name='criartarefa'),
    path('app/editartarefa/<int:pk>/', views.editartarefa, name='editartarefa'),
    path('app/apagartarefa/<int:pk>/', views.apagartarefa, name='apagartarefa'),
]
