from django.urls import path, include
from . import views


urlpatterns = [
 #path('', views.home, name="insurance"),
 path('', views.alliance, name="insurance"),
 path('predict', views.predictdisease, name="predictdisease"),
 path('team', views.team, name="team"),
 path('predict', views.predict, name="predict"),
 path('about', views.about, name="about"),
 #path('insurance/', views.insurance, name="insurance"),
 path('hey/', views.hey, name="hey"),
 path('insurance/', views.insurance, name="home_two"),




]