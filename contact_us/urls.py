from django.urls import path
from . import views


app_name='contact_us'



urlpatterns = [
    path("contact-us/about/", views.about, name="about"),
    path("", views.subscriber, name="subscriber"),

    # path("contact_us/cta/", views.about, name="cta"),


]