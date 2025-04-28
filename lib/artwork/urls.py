from django.urls import path
from .views.views import portfolio_landing, portfolio_entry

urlpatterns = [
    path('', portfolio_landing, name='portfolio_landing'),
    path('<slug:slug>/', portfolio_entry, name='portfolio_entry'),
]