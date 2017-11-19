from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'Calaveras$', views.JuegoCalaveras),
    url(r'EludeAsteroids$', views.JuegoEludeAsteroids),
    url(r'Llorona$', views.JuegoLlorona),
    url(r'2048$', views.juego2048),
 	url(r'Charizard$', views.juegocharizard),   
]