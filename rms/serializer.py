from rest_framework import serializers
from .models import Category
from .models import Food
 
class CategorySerilizers(serializers.ModelSerializer):
    class Meta:
        model = Category
        # serialize all model field or attribute 
        fields = '__all__' 
        
    def save(self,**kwargs):
        validated_data = (self.validated_data)
        # counting name (.count)
        category_count = self.Meta.model.objects.filter(name = validated_data.get('name')).count()
        if category_count > 0:
                raise serializers.ValidationError({
                    'details':"Category already exists"
                })
        category = Category(**validated_data)   # **validated data = it open the all data.
        category.save()
        return category
    
    
class FoodSerilizers(serializers.ModelSerializer):
        price_with_tax = serializers.SerializerMethodField()
        category = serializers.StringRelatedField()
        category_id = serializers.PrimaryKeyRelatedField(
            queryset = Category.objects.all(),
            source = 'category'
        )
        class Meta:
            model = Food
            fields = ['id','name','price','price_with_tax','category_id','category']
                                 
        def get_price_with_tax(self,food:Food):
            return food.price*0.10 + food.price
                
            
        