from rest_framework import serializers

from services.models import Subscription, Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('__all__')

###################### высчитываем цену в сериалайзере

# class SubscriptionSerializer(serializers.ModelSerializer):
#     plan = PlanSerializer()
#     client_name = serializers.CharField(source="client.company")   #возвращает название компании а не id
#     email = serializers.CharField(source="client.user.email")
#     price = serializers.SerializerMethodField()
#
#     def get_price(self, instance):
#         return instance.service.full_price - instance.service.full_price * (instance.plan.discount_percent / 100)
#
#
#     class Meta:
#         model = Subscription
#         fields = ['id', 'plan_id', 'client_name', 'email', 'plan', 'price']


class SubscriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    client_name = serializers.CharField(source="client.company")   #возвращает название компании а не id
    email = serializers.CharField(source="client.user.email")
    price = serializers.SerializerMethodField()

    def get_price(self, instance):
        return instance.price


    class Meta:
        model = Subscription
        fields = ['id', 'plan_id', 'client_name', 'email', 'plan', 'price']