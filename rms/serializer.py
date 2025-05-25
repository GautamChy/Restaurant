from rest_framework import serializers
from .models import Category
from .models import Food
from .models import Table
from .models import Order
from .models import OrderItem
 
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
        
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id','number','available']
        
class OrderItemSerializer(serializers.ModelSerializer):
    food_id = serializers.PrimaryKeyRelatedField(
        queryset = Food.objects.all(),
        source = 'food'
    )
    food = serializers.StringRelatedField()
    class Meta:
        model = OrderItem
        fields =['food_id','food']
        
class OrderSerializer(serializers.ModelSerializer):
    # Its hidden from the user input but required in the model
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    # Calling OrderItemSerializer(items)
    items = OrderItemSerializer(many=True)
    status = serializers.CharField(read_only=True)
    payment_status = serializers.CharField(read_only=True)
    class Meta:
        model = Order
        fields = ['user','total_price','status','payment_status','items']
        
        #Override create function
    def create(self,validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        
        for item in items_data:
            OrderItem.objects.create(order=order,food=item['food'])
        return order
            
        
    
   
                
            
        