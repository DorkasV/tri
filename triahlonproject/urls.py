"""triahlonproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('triathlon/', include('triathlon.urls')),
    # path('', RedirectView.as_view(url='/triathlon/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Triathlon Admin"
admin.site.site_title = "Triathlon Admin Portal"
admin.site.index_title = "Welcome to Triathlon Portal"

from triathlon import views

router = routers.DefaultRouter()
router.register(r'athletes', views.AthleteViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'results', views.ResultViewSet)
router.register(r'distances', views.DistanceViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'countries', views.CountryViewSet)
router.register(r'cities', views.CityViewSet)
router.register(r'teams', views.TeamViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/docs/', include_docs_urls(title='Tri API')),
]
