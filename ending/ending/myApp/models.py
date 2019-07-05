from django.db import models

# Create your models here.
class URLS(models.Model):
    url     =models.CharField(max_length=100)
    datetime=models.DateTimeField(auto_now=True)
    urlid   =models.CharField(max_length=45)
    short   =models.BooleanField(default=False)
    sqlin   =models.BooleanField(default=False)
    heartbl =models.BooleanField(default=False)
    eternalb=models.BooleanField(default=False)
    dns=models.BooleanField(default=False)
    def __str__(self):
        return self.url