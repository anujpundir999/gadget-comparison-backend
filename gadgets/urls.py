from django.urls import path
from .views import GadgetList, GadgetDetail

urlpatterns = [
    path('gadgets/', GadgetList.as_view(), name='gadget-list'),
    path('gadgets/<int:pk>/', GadgetDetail.as_view(), name='gadget-detail'),
]