from django.urls import path
from views import list_profits, add_profit, EditProfit

urlpatterns = [
    path('profits/', list_profits),
    path('add_profit/', add_profit),
    path('profit/<int:pk>/', EditProfit.as_view()),
]
