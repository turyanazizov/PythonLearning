from django.db import models

class Message(models.Model):

    SenderName = models.CharField(max_length=255)
    SenderEmail = models.CharField(max_length=255)
    SenderSubject = models.CharField(max_length=255)
    SenderContent = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.SenderName}'s message"
