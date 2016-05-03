from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import *
from forms import NewProductForm
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def store_list(request):
    products = Product.objects.order_by('catagory')
    return render(request, "store.html", {'products': products})


# def last_post(request):
#      posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#      last_post=posts[0]
#      return render(request, "index.html",{'last_post':last_post})

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {'product': product})


def new_product(request):
    if request.method == "POST":
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.published_date = timezone.now()
            product.save()
            return redirect(product_detail, product.pk)

    else:
        form = NewProductForm

    return render(request, 'newproductform.html', {'form': form})


def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = NewProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            #post.author = request.user
            product.published_date = timezone.now()
            product.save()
            return redirect(product_detail, product.pk)
    else:
        form = NewProductForm(instance=product)

    return render(request, 'newproductform.html', {'form': form})


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect(store_list)





# Create your views here.

@csrf_exempt
def paypal_return(request):
    args = {'post': request.POST, 'get': request.GET}
    # item=request.POST['payment_item']
    # amount=request.POST['payment_gross']
    # merchant=request.POST['reciever_email']


    return render(request, 'paypal_return.html', args)


def paypal_cancel(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal_cancel.html', args)
