from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.TextField()
    pub_date = models.DateField()
    summary =models.TextField(max_length=2000)
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title