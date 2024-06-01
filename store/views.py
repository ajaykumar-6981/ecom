from django.shortcuts import render,get_object_or_404
from .models import Product,Category,ReviewRating, ProductGallery

# Create your views here.
def store(request):

     # if category_slug != None:
     #      categories=get_object_or_404(Category)
     #      products=Product.objects.filter(category=categories, is_available=True)
     #      product_count=products.count()
     # else:
     #      products=Product.objects.all().filter(is_available=True)
     #      product_count=products.count()


     products = Product.objects.all()
     product_count=products.count(),
     return render(request,'store.html',{
          'products':products,
          'product_count':product_count

     })

def cart(request):
     pass

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e

    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = None
    else:
        orderproduct = None

    # Get the reviews
    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

    # Get the product gallery
    product_gallery = ProductGallery.objects.filter(product_id=single_product.id)

    context = {
        'single_product': single_product,
        'in_cart'       : in_cart,
        'orderproduct': orderproduct,
        'reviews': reviews,
        'product_gallery': product_gallery,
    }
    return render(request, 'store/product_detail.html', context)
