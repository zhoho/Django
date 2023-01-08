from django.urls import path
from myweb import views
urlpatterns = [
    path('',views.index),
    path('create/', views.create),
    path('read/<id>/', views.read)
]
