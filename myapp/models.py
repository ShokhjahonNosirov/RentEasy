from django.db import models
from django.contrib.auth.models import User
# Create your models here.

remont_choices = (
    ("Qoniqarli", "Qoniqarli"),
    ("Yaxshi", "Yaxshi"),
    ("Yevro", "Yevro"),
)

class Post(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE,)
    post_image = models.CharField(max_length=255)
    xona_soni = models.IntegerField()
    manzil = models.CharField(max_length=255)
    narx = models.IntegerField() # oldida sum tursin 
    body = models.CharField(max_length=255) # place holder > qulayliklar va hokazolar haqida batafsil ma'lumot bering
    yashash_maydoni = models.IntegerField() # oldida m2 tursin
    remont = models.CharField(max_length=255, choices=remont_choices, verbose_name = "remont status")
    etaj = models.IntegerField()
    kun = models.DateField()
    vaqt = models.TimeField()

    def __str__(self):
        return self.manzil




# class Profile(models.Model):
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     saved_courses = models.ForeignKey(Course, on_delete=models.CASCADE)