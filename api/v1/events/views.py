from rest_framework import generics
from rest_framework import views
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from api.model.event import Event
from .filters import EventFilter
from .serializers import EventSerializer


class EventDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'accident_number'

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return Response({'message': 'Event not found.'}, status=status.HTTP_404_NOT_FOUND)


class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.AllowAny,)
    filterset_class = EventFilter