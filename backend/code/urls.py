from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views

api_urls = [
    path('profits', views.list_profits),
    path('services', views.list_services),
    path('<int:pk>/add_consultation', views.add_consultation),
    path('sites', views.list_sites),
    path('advertisements', views.list_advertisements),
    path('add_application', views.add_application),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
