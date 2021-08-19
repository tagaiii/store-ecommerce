from specs.models import CategoryFeature, FeatureValidator, ProductFeatures
from django.contrib import admin

from .models import * 

admin.site.register(ProductFeatures)
admin.site.register(CategoryFeature)
admin.site.register(FeatureValidator)