from django.db import models
from django.utils.text import slugify

class TagLine(models.Model):
    caption = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.caption}'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Post(models.Model):
    card_title = models.CharField(max_length=100)
    card_description = models.TextField()
    img_url = models.ImageField(upload_to='images/', blank=True, null=True)
    event_date = models.DateField(auto_now=True, auto_now_add=False)  # For storing date only
    event_time = models.TimeField(auto_now=True, auto_now_add=False)  # For storing time only
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    slug = models.SlugField(max_length=255, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True)
    tags = models.ManyToManyField(TagLine,null=True)

    def save(self, *args, **kwargs):
        # self.created_at = slugify(f'{self.event_date} {self.event_time}')
        if not self.slug:
            self.slug = slugify(self.card_title)
            super().save(*args,**kwargs)

    def __str__(self):
        return self.card_title


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
       
        super().save(*args,**kwargs)

    def __str__(self):
        return f"Comment by {self.user_name} on {self.post}"