from django.db import models

# Create your models here.
class Job(models.Model):
    summary=models.CharField(max_length=2000)
    image=models.ImageField(upload_to='image/')

    def __str__(self):
            return self.summary
    