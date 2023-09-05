from django.urls import path
from product.views import product_list_view,product_detail_view
from page.views import  (
    home,
    oylesine_view,
    contact_us,
    vision_us,
    about_us,
    )

urlpatterns = [
    path("",product_list_view),
    path('<int:id>/',product_detail_view),
    

]
