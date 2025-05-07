from django.urls import path,include
from .views import CategoryAPIView,FoodAPIViewset,TableAPIViewset
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'categories',CategoryAPIView)
router.register(r'foods',FoodAPIViewset)
router.register(r'tables',TableAPIViewset)

urlpatterns = [
#     path('category',CategoryAPIView.as_view({'get':'list','post':'create'})),
#     path('category/<int:pk>/',CategoryAPIView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}))
 ] +router.urls