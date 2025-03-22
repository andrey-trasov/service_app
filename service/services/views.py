from django.db.models import Prefetch
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from services.models import Subscription
from services.serializers import SubscriptionSerializer

################ делает 1 запрос чтобы достать все записи по ключу, но возвращает все поля связанных моделей

# class SubscriptionView(ReadOnlyModelViewSet):
#     queryset = Subscription.objects.all().prefetch_related('client').prefetch_related('client__user')
#     serializer_class = SubscriptionSerializer


################ возвращает только нужные поля для связанных моделей

# class SubscriptionView(ReadOnlyModelViewSet):
#     queryset = Subscription.objects.all().prefetch_related(
#         Prefetch('client',
#                  queryset=Client.objects.select_related('user').only('company', 'user__email'))
#     )
#     serializer_class = SubscriptionSerializer


################ оптимизированные запрос с вложенным сериализатором

class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch('client',
                 queryset=Client.objects.select_related('user').only('company', 'user__email'))
    )
    serializer_class = SubscriptionSerializer