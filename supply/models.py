from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    profile_photo = models.ImageField(default='images/profiles/default.jpg', upload_to='images/profiles/')
    bio = models.TextField(max_length=500, null=True, blank=True)
    phone_number = models.CharField(max_length=10, unique=True)

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(id=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(id=id).first()
        return profile

    def __str__(self):
        return self.user.username


class Brand(models.Model):
    brand_name = models.CharField(max_length=20)
    brand_image = models.ImageField(upload_to="images/brand/")

    def __str__(self):
        return self.brand_name


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    Product_Categories = [
        ('Balls', 'images/brand/balls.jpeg'),
        ('Rackets', 'images/brand/rackets.jpeg'),
        ('Apparel', 'images/brand/apparel.jpeg'),
    ]
    images = models.ImageField(upload_to='images/product/')
    item_name = models.CharField(max_length=20)
    item_description = models.TextField(max_length=200, verbose_name="Item Description")
    item_price = models.FloatField(default=0.00)
    slug = models.SlugField(null=True, unique=True)
    item_details = models.TextField(max_length=1000, verbose_name="Item Details")
    item_quantity = models.IntegerField(default=0)
    item_availability = models.BooleanField(default=False)
    item_brand = models.ForeignKey(Brand, null=True)
    item_categories = models.ForeignKey(Category, null=True)

    def __str__(self):
        return self.item_name

    def save_product(self):
        return self.save()

    class Meta:
        ordering = ['item_name']
