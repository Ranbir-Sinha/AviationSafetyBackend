import django_filters.filters

from api.model.event import Event


class EventFilter(django_filters.FilterSet):
    year = django_filters.filters.NumberFilter(field_name='event_date__year', lookup_expr='exact')
    accident_number = django_filters.filters.CharFilter(field_name='accident_number', lookup_expr='exact')
    country = django_filters.filters.CharFilter(field_name='country', lookup_expr='exact')

    class Meta:
        model = Event
        fields = ['year', 'accident_number', 'country']
