from django.db import models

# Create your models here.
DEFAULT_STATUS = "draft"
STATUS = (
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),      
)

class Page(models.Model):
    #title: 
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,default="",) 
    content = models.TextField()
    cover_image = models.ImageField(null=True, blank=True, upload_to='page',)
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class Carousel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    cover_image = models.ImageField(null=True, blank=True, upload_to='carousel',)
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)