from django.db import models

# Create your models here.
class About(models.Model):
    hello = models.CharField(max_length=200)
    about_text = models.TextField()
    about_image = models.ImageField(upload_to='folio/images/', default='folio/images/default.jpg')

    def __str__(self):
        return self.hello
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    start_year = models.IntegerField()
    description = models.TextField()
    url = models.URLField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    image = models.ImageField(upload_to='folio/images/', default='folio/images/default.jpg')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')

class Experience(models.Model):
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    main_tech = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class ExperienceTechnology(models.Model):
    name = models.CharField(max_length=200)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='technologies')

    def __str__(self):
        return self.name