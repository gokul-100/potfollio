from django.db import models
from django.utils.text import slugify



class Post(models.Model):
    card_title = models.CharField(max_length=100)
    card_description = models.TextField()
    img_url = models.ImageField(upload_to='images/', blank=True, null=True)
    event_date = models.DateField(auto_now=True, auto_now_add=False)  # For storing date only
    event_time = models.TimeField(auto_now=True, auto_now_add=False)  # For storing time only
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    slug = models.SlugField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # self.created_at = slugify(f'{self.event_date} {self.event_time}')
        if not self.slug:
            self.slug = slugify(self.card_title)
            super().save(*args,**kwargs)

    def __str__(self):
        return self.card_title

# Create your models here.
