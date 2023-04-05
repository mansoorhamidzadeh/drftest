from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class drfTest(models.Model):
    LANGUAGE_CHOICES = (
        ('p', 'python'),
        ('j', 'java'),
    )
    owner=models.ForeignKey(User,related_name='drftest',on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    code = models.TextField()
    line = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
