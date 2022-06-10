from django.db import models

class AboutSection(models.Model):
    STATUS_CHOICES = (
        ('Inactive', 'Inactive'),
        ('Active', 'Active'),
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='about/')
    status = models.CharField(max_length=255,default=True,choices=STATUS_CHOICES)

    def __str__(self):
        return self.title