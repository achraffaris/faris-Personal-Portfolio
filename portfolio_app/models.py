from django.db import models
from djrichtextfield.models import RichTextField

# Create your models here.
class Project(models.Model):
    date = models.DateField(null=True,auto_now_add=True)
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300,null=True,blank=True)
    frontend = models.CharField(max_length=150,null=True,blank=True)
    backend = models.CharField(max_length=150,null=True,blank=True)
    image = models.ImageField(upload_to="projects")
    live_demo = models.URLField(null=True, max_length=200)
    source_code = models.URLField(null=True, max_length=200)
    description = RichTextField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def viewed(self):
        self.views += 1
        self.save()
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="categories")
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    category = models.ForeignKey("Category", verbose_name="categories", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    date = models.DateField(null=True,auto_now_add=True)
    views = models.IntegerField(default=0)

    def viewed(self):
        self.views += 1
        self.save()

    def __str__(self):
        return self.title

class Education(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=150)
    school = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.school
class Experience(models.Model):
    start = models.DateField()
    end = models.DateField()
    title = models.CharField(max_length=150)
    campany = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.campany
class Certificate(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=150)
    organization = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.organization
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=350)
    message = models.TextField(max_length=1000)
    def __str__(self):
        return self.subject