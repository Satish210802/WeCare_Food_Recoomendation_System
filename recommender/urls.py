from django.contrib import admin
from django.urls import path
from recommender import views

urlpatterns = [
    path("", views.home, name='home1'),
    path("login1", views.login_view, name='login'),
    path("login" ,views.login_view,name="login1"),
    path("logout",views.logout_view,name ='logout'),
    path("home", views.home, name="home"),
    path("bodymass",views.bodymass,name="bodymass"),
    path("dietplanner",views.index,name="dietplanner"),
    path("diet",views.diet,name="diet"),
    path("Dashboard",views.Dashboard,name="Dashboard"),
    path("satish",views.satish,name="satish"),
    path("koustubh",views.koustubh,name="koustubh"),
    path("sagar",views.sagar,name="sagar"),
    path("saurabh",views.saurabh,name="sagar"),
    path("team",views.team,name="team"),
    path("contact", views.contact, name="contact"),
    path("profile", views.profile, name="profile"),
]