from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexTemplateView

from . import views

urlpatterns = [
    path("", IndexTemplateView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
