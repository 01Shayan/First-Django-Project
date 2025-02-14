from django.db import models
from django.contrib.auth.models import User
from django.core.validators import ValidationError
from datetime import datetime


class Account(models.Model):
    
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]

    def check_gender(value):
        if value not in ["F", "M"]:
            raise ValidationError("Gender must be Female or Male")
        
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to="avatar/", null=True, blank=True)
    father_name = models.CharField(max_length=30, null=True, blank=True)
    age = models.SmallIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="-", blank=True)
    phone = models.CharField(null=True, blank=True, max_length=15)
    national_code = models.CharField(max_length=10, null=True, blank=True, verbose_name="National Code")
    address = models.TextField(null=True, blank=True)
    postal_code = models.CharField(max_length=15, null=True, blank=True)
    joined_date = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = "accounts"
        verbose_name = "accounts"
        verbose_name_plural = "accounts"
    
    def __str__(self):
        return f"{str(self.user_id).title()} - id({str(self.user_id.id)})"
