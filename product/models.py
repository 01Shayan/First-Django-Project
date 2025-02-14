from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=30)

    class Meta:
        db_table = "products_category"


class Sub_Category(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=30)
    parent = models.OneToOneField(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "products_sub_category"


class Product(models.Model):
    # product_name = models.CharField(max_length=30)
    # user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    # count = models.IntegerField()
    # price = models.BigIntegerField()
    # photo = models.ImageField(upload_to="product/", null=True, blank=True)
    # description = models.TextField(max_length=300)
    # details = models.JSONField()
    # category = models.OneToOneField(Sub_Category, on_delete=models.CASCADE)

    product_name = models.CharField(max_length=30, verbose_name="نام محصول")
    count = models.SmallIntegerField(default=0, blank=True, null=False, verbose_name="تعداد محصول")
    price = models.IntegerField(default=0, blank=True, null=False, verbose_name="قیمت محصول")
    category = models.OneToOneField(Sub_Category,
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL,
                                    verbose_name="نام دسته بندی")
    photo = models.ImageField(upload_to="product/", blank=True, null=True,
                              verbose_name="عکس محصول")
    details = models.JSONField(verbose_name="جزئیات محصول", null=True, blank=True)
    description = models.TextField(verbose_name="توضیحات محصول", null=True, blank=True)
    user_id = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)


    class Meta:
        db_table = "products"
