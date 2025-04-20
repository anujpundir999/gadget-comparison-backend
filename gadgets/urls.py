from django.urls import path
from .views import GadgetList, GadgetDetail,get_tech_news

urlpatterns = [
    path('gadgets/', GadgetList.as_view(), name='gadget-list'),
    path('gadgets/<int:pk>/', GadgetDetail.as_view(), name='gadget-detail'),
    path('gadgets/technews/', get_tech_news, name='tech_news'),
]