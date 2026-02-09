from django.shortcuts import render 
from .models import Product, Category
# Create your views here.



def get_products(request):
    all_products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'products.html', {"products":all_products, "categories":categories})



def detail(request, id):
    product_id = id
    detail = Product.objects.get(id=product_id)

    
    return render(request, "detail.html", {"products":detail})



def search_product(request):
    query = request.POST.get("query")
    product = Product.objects.filter(name__contains=query)
    return render(request, "result.html", {"results":product})



def filter_category(request):
    category_id = request.POST.get("category_id")
    categories = Category.objects.all()
    
    if category_id != '0':

        natija = Product.objects.filter(category = category_id)
    else: 
        natija = Product.objects.all()
        

    return render(request, "products.html", {"products":natija, "categories":categories})
