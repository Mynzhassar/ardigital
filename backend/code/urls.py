from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('profits/', views.profit_views.list_profits),
    path('add_profit/', views.profit_views.add_profit),
    path('profit/<int:pk>/', views.profit_views.EditProfit.as_view()),

    path('services/', views.service_views.list_services),
    path('add_service/', views.service_views.add_service),
    path('service/<int:pk>/', views.service_views.EditService.as_view()),

    path('consultations/', views.consultation_views.list_consultations),
    path('add_consultation/', views.consultation_views.add_consultation),
    path('consultation/<int:pk>/', views.consultation_views.EditConsultation.as_view()),

    path('sites/', views.site_views.list_sites),
    path('add_site/', views.site_views.add_site),
    path('site/<int:pk>/', views.site_views.EditSite.as_view()),

    path('advertisements/', views.advertisement_views.list_advertisements),
    path('add_advertisement/', views.advertisement_views.add_advertisement),
    path('advertisement/<int:pk>/', views.advertisement_views.EditAdvertisement.as_view()),
]
