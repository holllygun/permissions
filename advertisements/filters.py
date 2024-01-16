from django_filters import rest_framework as filters, DateFromToRangeFilter, ChoiceFilter, NumberFilter

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()
    status = ChoiceFilter(field_name='status', choices=AdvertisementStatusChoices.choices)
    creator = NumberFilter(field_name='creator_id')
    filterset_fields = ['status', 'creator']

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator']
    # TODO: задайте требуемые фильтры

