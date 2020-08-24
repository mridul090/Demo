from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Content(models.Model):
  Title = models.CharField(max_length=255,blank=True)
  Description = models.TextField('Describ')
  content_image = models.ImageField(upload_to='Content/', blank=True)
  author = models.ForeignKey(User,default=None)

class Slider(models.Model):

  photo_1 = models.ImageField(upload_to='sliderImage/', blank=True)
  photo_1_header =models.CharField(max_length=100)
  photo_1_details=models.CharField(max_length=100)

  photo_2 = models.ImageField(upload_to='sliderImage/', blank=True)
  photo_2_header =models.CharField(max_length=100)
  photo_2_details=models.CharField(max_length=100)

  photo_3 = models.ImageField(upload_to='sliderImage/', blank=True)
  photo_3_header =models.CharField(max_length=100)
  photo_3_details=models.CharField(max_length=100)

  author = models.ForeignKey(User,default=None)


class OurTeam(models.Model):
  Photo_1 = models.ImageField(upload_to='OurTeam/', blank=True)
  Name1 = models.CharField(max_length=150)
  Designation1 = models.CharField(max_length=200)
  Details1 = models.CharField(max_length=600)

  Photo_2 = models.ImageField(upload_to='OurTeam/', blank=True)
  Name2 = models.CharField(max_length=150)
  Designation2 = models.CharField(max_length=200)
  Details2 = models.CharField(max_length=600)

  #author = models.ForeignKey(User,default=None)


class ProgressBer(models.Model):
    First = models.IntegerField()
    First_description = models.CharField(max_length=30)
    Second = models.IntegerField()
    Second_description = models.CharField(max_length=30)
    Third = models.IntegerField()
    Third_description = models.CharField(max_length=30)
    Fourth = models.IntegerField()
    Fourth_description = models.CharField(max_length=30)

    author = models.ForeignKey(User,default=None)


class Testimonial(models.Model):
    Details = models.TextField(blank=True)
    Name =  models.CharField(max_length=40)
    Designation = models.CharField(max_length=30)
    author = models.ForeignKey(User,default=None)
