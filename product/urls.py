from django.urls import path
from . import views


app_name='product'



urlpatterns = [
    # path('', views.index_product, name='home'),
    path("product", views.product_index, name="product_index"),
    path("product/new/", views.new_product, name="new_product"),
    path("product/list/", views.list_product, name="list_product"),
]