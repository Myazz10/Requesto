from django.contrib import admin
from .models import VisitorMetaData, TestMetaData, TestCityData


admin.site.register(TestMetaData)
admin.site.register(TestCityData)
admin.site.register(VisitorMetaData)
