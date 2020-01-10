from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_photo = models.ImageField(default='default.jpg', upload_to='profiles/')
    # bio = models.TextField(max_length=500,default='Tell Me Something')
    # website = models.CharField(max_length=10, blank=True,default='me.com')
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=10, default=12345678)

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
        return self.title

    from django.db.models.signals import post_save


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=45)

    def __str__(self):
        return self.Name

    def save_image(self):
        return self.save()

    class Meta:
        ordering = ['image']
