from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class BlogModel(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    blogtitle = models.CharField(max_length = 100)
    blogdesc = models.TextField(max_length = 200)
    blogimg = models.ImageField(upload_to = 'pics')
    date = models.DateField(auto_now = True)
    time = models.TimeField(auto_now = True)

    def __str__(self):
        return self.blogtitle

    def __str__(self):
        return self.date

    def __str__(self):
        return self.time

    class Meta:
        db_table = 'blog_table'