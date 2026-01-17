from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .managers import ItemManager
from django.utils import timezone 

# Create your models here.
class Item(models.Model):

    class Meta:
        indexes = [
            models.Index(fields=['user', 'item_price'])
        ]

    def __str__(self):
        return self.item_name + ":" + str(self.item_price)
    
    def get_absolute_url(self):
        return reverse('MyApp:index')
    
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200, db_index=True)
    item_desc = models.CharField(max_length=200)
    item_price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    item_image = models.URLField(max_length=600, default='https://grandseasonscoquitlam.com/img/placeholders/comfort_food_placeholder.png')
    is_avaible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)


    objects = ItemManager()
    all_objects = models.Manager()  

class Category(models.Model):
    name = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name