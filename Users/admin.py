from django.contrib import admin
from Users.models import user,product,ordered
# Register your models here.
class user_admin(admin.ModelAdmin):
    list_display=('uname','email','password','address','pic','user_type','user_auth')

class product_admin(admin.ModelAdmin):
    list_display=('name','details','product_price','product_type','product_added_time','product_offers','pic','pic2','pic3','pic4','pic5','edoc')

class orders(admin.ModelAdmin):
    list_display=('uid','umail','order_name','order_details','ex_order_delevery','ex_order_delevery_time','order_date')


admin.site.register(user,user_admin)
admin.site.register(product,product_admin)
admin.site.register(ordered,orders)