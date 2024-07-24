"""
URL configuration for tasly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from produits import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accueil/", views.produit, name='accueil'),
    path("detail/", views.details, name="Produitdetails"),
    path("tuto_video/", views.tuto_video, name="tuto_video"),
    path("services/", views.Services, name="services"),
    path("tuto_audio/", views.tuto_audio, name="tuto_audio"),
    path("<int:id>", views.prod_paiement, name="prod_paiements"),
    path("<int:id>/", views.service_paiement, name="service_paiements"),
    path("validations/", views.validation_paiement, name="Validations"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)