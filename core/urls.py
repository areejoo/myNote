from django.urls import path
from .views import NoteApi

urlpatterns = [
    path('api',NoteApi.as_view(),name='api'),
]
