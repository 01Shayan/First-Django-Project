from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse



def product_index(req):
    if not req.user.is_authenticated:
        return redirect(reverse("account:login"))
    template="product_index.html"
    return render(req, template)


def new_product(req):
    if not req.user.is_authenticated:
        return redirect(reverse("account:login"))
    if req.method == "POST":
        product_name = req.POST.get("product_name", False)
        image_product = req.FILES.get("image_product", False)
        if image_product and product_name:
            from .models import Product
            p = Product()
            p.product_name = product_name
            p.photo = image_product
            p.save()
    elif req.method == "GET":
        from .models import Product
        p = Product.objects.all()
        template="new_product.html"
        return render(req, template, {"products": p})
    else:
        return HttpResponse("Boro BaBa", status=404)
    return redirect(reverse("product:product_index"))


def list_product(req):
    if not req.user.is_authenticated:
        return redirect(reverse("account:login"))
    template="list_product.html"
    return render(req, template)