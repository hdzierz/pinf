# -*- coding: utf-8 -*-

import django_filters
from api.models import FishOb


class FishObFilter(django_filters.FilterSet):
    class Meta:
        model = FishOb
        fields = ['xreflsid']
        order_by = ['xreflsid']