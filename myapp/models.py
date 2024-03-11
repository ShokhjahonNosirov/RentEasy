from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Post(models.Model):
    post_image = models.CharField(max_length=255)
    xona_soni = models.IntegerField()
    manzil = models.CharField(max_length=255)
    narx = models.IntegerField()
    snippet = models.CharField(max_length=255)
    kun = models.DateField()
    vaqt = models.TimeField()

    def __str__(self):
        return self.manzil




# class Profile(models.Model):
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     saved_courses = models.ForeignKey(Course, on_delete=models.CASCADE)