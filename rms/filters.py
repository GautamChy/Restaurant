from django_filters import FilterSet
from .models import Food
#from .models import Category

class FoodFilter(FilterSet):
    class Meta:
        model = Food
        fields = {
            'category':['exact'],
            'price':['gte','lte']
        }
        

