from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500,default='Title')
    subtitle = models.CharField(max_length=500,default='Subtitle')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title


