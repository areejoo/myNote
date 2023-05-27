from django.db import models
import datetime

class Author(models.Model):
    
    full_name=models.CharField(max_length=50,default='')
    nick_name =models.CharField(max_length=50, null=True, blank=True)
    email =models.EmailField(default='admin@admin.com')
    profile_photo =models.ImageField(upload_to="myNote/photos",null=True ,blank=True)

    def __str__(self):
        return self.full_name
    
class Note(models.Model):

    author = models.ForeignKey(Author ,related_name='authors',on_delete=models.CASCADE)
    title = models.CharField(max_length=255,default='   ')
    content = models.TextField(default='')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
