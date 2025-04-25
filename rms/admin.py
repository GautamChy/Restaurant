from django.contrib import admin
from .models import Category,Food,Table,Order,OrderItem

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_filter = ('name',)
    search_fields = ('name',)
admin.site.register(Category,CategoryAdmin)      
    
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','category')
    list_filter = ('name','category')
    search_fields = ('name',)
    list_per_page = 10
    autocomplete_fields = ('category',) 
       
admin.site.register(Food,FoodAdmin)

class TableAdmin(admin.ModelAdmin):
    list_display = ('number','available')
    list_filter = ('available',)
    list_editable = ('available',)
    
admin.site.register(Table,TableAdmin)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    autocomplete_fields = ('food',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','total_price','status','payment_status')
    list_filter = ('status','payment_status')
    search_fields = ('user__username',)
    list_editable = ('status','payment_status')
    inlines = [OrderItemInline]
    
admin.site.register(Order,OrderAdmin)

#class OrderItemAdmin(admin.ModelAdmin):
    #list_display = ('food','order')
    #list_filter = ('order',)
    #search_fields = ('order',)
#admin.site.register(OrderItem,OrderItemAdmin)