from django.db import models

class Realtor(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos/%Y%m/%d/", blank=True)
    description = models.TextField()
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name