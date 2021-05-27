from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=200)
    Mobile = models.CharField(max_length=200)
    Email= models.CharField(max_length=200)
    # author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
 
    Message = models.TextField()
   
    

    def __str__(self):
        return self.title
