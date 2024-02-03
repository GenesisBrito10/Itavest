from django.urls import path
from .views import BordadoListCreateView, BordadoRetrieveUpdateDeleteView

urlpatterns = [
    path('bordados/', BordadoListCreateView.as_view(), name='bordado-list-create'),
    path('bordados/<int:pk>/', BordadoRetrieveUpdateDeleteView.as_view(), name='bordado-retrieve-update-delete'),
]
