from datetime import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.model.event import Event
from api.v1.events.serializers import EventSerializer


class EventListTestCase(APITestCase):
    def setUp(self):
        self.event1 = Event.objects.create(
            event_id='1',
            accident_number='12345',
            country="US",
            event_date=datetime(2019, 12, 31))
        self.event2 = Event.objects.create(
            event_id='2',
            accident_number='54321',
            country="US",
            event_date=datetime(2018, 12, 31))

    def test_get_all_events(self):
        url = reverse('event-list')
        response = self.client.get(url)
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    def test_get_single_event_by_accident_number(self):
        url = reverse('event-list') + '12345/'
        response = self.client.get(url)
        event = Event.objects.get(accident_number='12345')
        serializer = EventSerializer(event)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_filtered_events_by_country(self):
        url = reverse('event-list') + '?country=US'
        response = self.client.get(url)
        events = Event.objects.filter(country='US')
        serializer = EventSerializer(events, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)

    def test_get_filtered_events_by_year(self):
        url = reverse('event-list') + '?year=2019'
        response = self.client.get(url)
        events = Event.objects.filter(event_date__year=2019)
        serializer = EventSerializer(events, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)
