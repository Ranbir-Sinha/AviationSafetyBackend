from django.urls import path, include

urlpatterns = [
    path('events/', include('api.v1.events.urls'))
]