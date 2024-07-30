from django.db import models

# Create your models here.
class Image(models.Model):
    
    previewURL=models.URLField()
    largeImageURL=models.URLField()
    tags=models.CharField(max_length=100)
    likes=models.IntegerField()
    downloads=models.IntegerField(null=False, default=0)
    views=models.IntegerField(null=False, default=0)
    comments=models.IntegerField(null=False, default=0)  

    def __str__(self):
        return self.tags


