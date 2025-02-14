from django.db import models
from datetime import datetime



class Subscriber(models.Model):
    email = models.EmailField(max_length=255, null=True, blank=True)
    subscribe_date = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = "subscribers_email"

    def __str__(self):
        return str(self.email)


# class Cta(models.Model):
#     email = models.EmailField(max_length=255, null=True, blank=True)
#     subscribe_date = models.DateTimeField(default=datetime.now())
#
#     class Meta:
#         db_table = "cta"
#
#     def __str__(self):
#         return str(self.email)
