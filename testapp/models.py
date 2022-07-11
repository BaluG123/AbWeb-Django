from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Sports(models.Model):
    title=models.CharField(max_length=1000)
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-created']    

class Entertainment(models.Model):
    title=models.CharField(max_length=1000)
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-created']   

class Technology(models.Model):
    title=models.CharField(max_length=1000)
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-created']   

class EditorChoice(models.Model):
    title=models.CharField(max_length=1000)
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-created']           


