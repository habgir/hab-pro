from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    auther = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) :
        return self.title,self.auther
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})