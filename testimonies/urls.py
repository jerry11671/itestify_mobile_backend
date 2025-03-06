from django.urls import path
from .views import AddTextTestimonyAPIView


urlpatterns = [
    path("texts/create_text", AddTextTestimonyAPIView.as_view, name="add-text-testimony")
]
