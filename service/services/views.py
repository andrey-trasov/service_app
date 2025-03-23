from django.db.models import Prefetch, F, Sum
from django.http import request
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
    ).annotate(price=F('service__full_price') -
                     F('service__full_price') * F('plan__discount_percent') / 100.00)    # вычисление цены (влоденный сериализатор)
    serializer_class = SubscriptionSerializer


# добавляем к общему ответу поле total_amount с суммой цены всех подписок
    def list(self, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)

        response_data = {'result': response.data}
        response_data['total_amount'] = queryset.aggregate(total=Sum('price')).get('total')
        response.data = response_data

        return response

