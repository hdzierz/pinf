# -*- coding: utf-8 -*-

import django_filters
from api.models import FishOb


class FishObFilter(django_filters.FilterSet):
    class Meta:
        model = FishOb
        fields = ['xreflsid']
<<<<<<< HEAD
        order_by = ['xreflsid']
=======
        order_by = ['xreflsid']
>>>>>>> 8e3c934414cd4685ee33567a70b87c060ca9aea5
