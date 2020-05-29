from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=36,null=False,blank=False)
    description = models.TextField(max_length=256,blank=True)
    price = models.FloatField(default=0)
    published = models.DateField(blank=True,null=True,default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/',blank=True,)

    def __str__(self):
        return self.title

