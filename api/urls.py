from unicodedata import name
from django.urls import path
from . import views, auth_views

urlpatterns = [
    path('', auth_views.google_login),
    path('google/', auth_views.google_auth),
    path('user/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),
   
    path('prize/', views.PrizeView.as_view()),

    path('concorso/', views.ConcorsoView.as_view({'get': 'list', 'post': 'create'}), name='concorso'),
    path('concorso/<int:pk>/', views.ConcorsoView.as_view({'put': 'update', 'delete': 'destroy'})),

    path('winer/', views.WinerView.as_view({'get': 'list', 'post': 'create'}), name='winer'),
    path('winer/<int:pk>/', views.WinerView.as_view({'put': 'update', 'delete': 'destroy'})),

    path('play/<int:pk>/', views.PlayView.as_view()),
  
]