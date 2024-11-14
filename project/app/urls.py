from django.urls import path
from . import views

urlpatterns = [
    path('rewrite-text/', views.rewrite_view, name='rewrite-text'),
]
