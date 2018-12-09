from django.db import models

# Create your models here.

class Snippet(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    code = models.TextField()
    language = models.CharField(max_length=100,blank=True,null=True)
    style = models.CharField(max_length=100,blank=True,null=True)

    class Meta:
        ordering = ("title",)



