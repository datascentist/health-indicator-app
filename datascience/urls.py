from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("heart", views.heart, name="heart"),
    path("diabetes", views.diabete_prediction, name="diabete_prediction"),
    path("predict_user_input", views.predict_user_input, name="predict_user_input"),
    path("visualisation-heart-000", views.embed_chart, name="embed_chart"),
    path("support", views.contact, name="contact"),
    path('sendMessage', views.sendMessage, name="sendMessage")
]
