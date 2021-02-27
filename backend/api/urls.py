from django.urls import path
from .views import profit_views, service_views

urlpatterns = [
    path('profits/', profit_views.list_profits),
    path('add_profit/', profit_views.add_profit),
    path('profit/<int:pk>/', profit_views.EditProfit.as_view()),

    path('services/', service_views.list_services),
    path('add_service/', service_views.add_service),
    path('service/<int:pk>/', service_views.EditService.as_view()),
]