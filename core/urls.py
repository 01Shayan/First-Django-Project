from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin page --> secret
    path("secret/", admin.site.urls),

    path("", include("account.urls", namespace="account")),
    path("", include("product.urls", namespace="product")),
    path("", include("contact_us.urls", namespace="contact_us")),
    path("", include("pwa.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
