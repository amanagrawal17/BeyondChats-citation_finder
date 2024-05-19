from django.urls import path
from .views import get_citations

urlpatterns = [
    path('citations/', get_citations, name='get_citations'),
]