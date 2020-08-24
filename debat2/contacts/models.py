from django.db import models

# Create your models here.
class contact_req(models.Model):
    name = models.CharField(max_length=255,blank=True)
    Email = models.EmailField(max_length=254,blank=True)
    Message = models.TextField('Message')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date)
