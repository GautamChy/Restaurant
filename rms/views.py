from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializer import CategorySerilizers,FoodSerilizers
from rest_framework.serializers import ValidationError
from .models import OrderItem
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
#from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import Food
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters import rest_framework as filter
from .filters import FoodFilter

# Create your views here
class CategoryAPIView(ModelViewSet):
      queryset = Category.objects.all()
      serializer_class = CategorySerilizers
      
        # overide  list inside ModelViewSet
      def list(self,request):
          queryset = Category.objects.all()
          serializer = CategorySerilizers(queryset,many=True)
          return Response({'data':serializer.data})
        
        #overide  destroy inside ModelViewSet
      def destroy(self,request,id):
          category = get_object_or_404(Category,id=id)
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
          
     

         
         
         
      
      
      
    
    
       
          
   
    
    
       
         
       
     
      
       
   
   





