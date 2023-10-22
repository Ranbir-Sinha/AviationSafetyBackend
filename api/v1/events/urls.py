from django.urls import path
from .views import EventDetail, EventList

urlpatterns = [
    path('', EventList.as_view(), name='event-list'),
    path('<str:accident_number>/', EventDetail.as_view(), name='event-detail')
]
