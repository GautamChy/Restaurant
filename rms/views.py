from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializer import CategorySerilizers,FoodSerilizers,TableSerializer,OrderSerializer
from rest_framework.serializers import ValidationError
from .models import OrderItem
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Food
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters import rest_framework as filter
from .filters import FoodFilter
from .models import Table
from .serializer import TableSerializer
from .permission import IsAuthenticatedOrReadonly
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from .models import Order


# Create your views here
class CategoryAPIView(ModelViewSet):
      queryset = Category.objects.all()
      serializer_class = CategorySerilizers
      pagination_class = PageNumberPagination
      
      #Overide  list inside ModelViewSet
      @extend_schema(
            parameters=[
                  OpenApiParameter(name='name', description='Filter by name', required=False, type=str),],
                  description='This is the category list',)
      def list(self,request):
            # Fetches the query parameter name from the request URL 
            name =request.GET.get('name')
            if name:
                  category = Category.objects.filter(name=name)
                  serializer = CategorySerilizers(category,many=True)
                  # Returns the serialized data as a JSON response
                  return Response(serializer.data)
            #If no name is provide then this call the default list method from ModelViewSet
            return super().list(request)
                  
            
       #Overide  destroy inside ModelViewSet     
      def destroy(self,request,pk):
          category = get_object_or_404(Category,id=pk)
          count = OrderItem.objects.filter(food__category = category).count()
          if count > 0:
            return Response({
              "detail": "OrderItem with this category exist.This category cannot be deleted."
            })
          category.delete()
          return Response({
         "detail":"This category is deleted"
         },status=status.HTTP_204_NO_CONTENT)
          
class FoodAPIViewset(ModelViewSet):
      # select_related work to reduce time.
      queryset = Food.objects.select_related().all()
      serializer_class = FoodSerilizers
      pagination_class = PageNumberPagination
      filter_backends = [filters.SearchFilter,filter.DjangoFilterBackend]
      search_fields = ('name',)
      filterset_class = FoodFilter
      permission_classes = [IsAuthenticatedOrReadonly]
      
class TableAPIViewset(ModelViewSet):
      queryset = Table.objects.all()
      serializer_class = TableSerializer
      pagination_class = PageNumberPagination
      filter_backends = [filters.SearchFilter]
      search_fields =['id','number','available']
      permission_classes = [IsAuthenticatedOrReadonly]
      
class OrderViewSet(ModelViewSet):
      queryset = Order.objects.prefetch_related('items').all()
      serializer_class = OrderSerializer
      #pagination_class = PageNumberPagination
      #permission_classes = [IsAuthenticated]
      

      
     
      
      
      

      
     
      
      
      
      

# class CategoryList(ListCreateAPIView):
#       queryset = Category.objects
#       serializer_class =  CategorySerilizers
       
# class CategoryDetail(RetrieveUpdateDestroyAPIView):
#       queryset = Category.objects
#       serializer_class =  CategorySerilizers
#       lookup_field = 'id'
      
#        # overide 
#       def destroy(self,request,id):
#           category = get_object_or_404(Category,id=id)
#           count = OrderItem.objects.filter(food__category = category).count()
#           if count > 0:
#             return Response({
#               "detail": "OrderItem with this category exist.This category cannot be deleted."
#             })
#           category.delete()
#           return Response({
#          "detail":"This category is deleted"
#          },status=status.HTTP_204_NO_CONTENT)
          
     

         
         
         
      
      
      
    
    
       
          
   
    
    
       
         
       
     
      
       
   
   





