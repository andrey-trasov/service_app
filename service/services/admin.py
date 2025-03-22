from django.contrib import admin

from services.models import Service
from services.models import Plan
from services.models import Subscription

admin.site.register(Service)
admin.site.register(Plan)
admin.site.register(Subscription)
