from django.db import models
from django.conf import settings
from django.urls import reverse
class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)
     #use CASCADE for the on_delete parameter so that related images are also deleted when a user is deleted.
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,
                               db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name='images_liked',
                                    blank=True)
    
    # many-to-many relationship in this case because a user might like multiple images and each image can be liked by multiple users.                             
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
      # slugify() function provided by Django to automatically generate the image slug for the given title when no slug is provided

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])