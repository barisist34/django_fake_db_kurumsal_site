from django.shortcuts import render
from .fake_db.products import FAKE_DB_PRODUCTS

# Create your views here.

def product_list_view(request):
    context=dict(
        products=FAKE_DB_PRODUCTS
    )

    return render(request,"product/products.html",context)