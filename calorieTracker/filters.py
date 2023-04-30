import django_filters
from django_filters import CharFilter
from .models import *

class MealFilter(django_filters.FilterSet):
    food_name = CharFilter(field_name = 'name',lookup_expr =      'icontains',label='search for meal')
    class Meta:
        model = Meal
        fields = ['name']