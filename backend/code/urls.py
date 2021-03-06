from django.contrib import admin
from django.urls import path, include

from . import views

profit_urls = [
    path('profits', views.profit_views.list_profits),
    path('add_profit', views.profit_views.add_profit),
    path('profit/<int:pk>', views.profit_views.EditProfit.as_view()),
]

service_urls = [
    path('services', views.service_views.list_services),
    path('add_service', views.service_views.add_service),
    path('service/<int:pk>', views.service_views.EditService.as_view()),
]

consultation_urls = [
    path('consultations', views.consultation_views.list_consultations),
    path('<int:pk>/add_consultation', views.consultation_views.add_consultation),
    path('consultation/<int:pk>', views.consultation_views.EditConsultation.as_view()),
]

site_urls = [
    path('sites', views.site_views.list_sites),
    path('add_site', views.site_views.add_site),
    path('site/<int:pk>', views.site_views.EditSite.as_view()),
]

advertisement_urls = [
    path('advertisements', views.advertisement_views.list_advertisements),
    path('add_advertisement', views.advertisement_views.add_advertisement),
    path('advertisement/<int:pk>', views.advertisement_views.EditAdvertisement.as_view()),
]

application_urls = [
    path('applications', views.application_views.list_applications),
    path('add_advertisement', views.application_views.add_application),
    path('advertisement/<int:pk>', views.application_views.EditApplication.as_view()),
]

api_urls = profit_urls + service_urls + consultation_urls + site_urls + advertisement_urls + \
           application_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls))
]
