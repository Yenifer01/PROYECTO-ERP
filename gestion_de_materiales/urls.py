from django.urls import path
from .views import MaterialListCreateView, MaterialDetailView

urlpatterns = [
    path('material/', MaterialListCreateView.as_view(), name='material-list-create'),
    path('material/<int:pk>/', MaterialDetailView.as_view(), name='material-detail'),
]
