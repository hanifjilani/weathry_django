from django.db import models

# Create your models here.
class Email(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=254)
    subject = models.CharField(max_length=120)
    text_area = models.TextField()
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.email_id + " - " + self.subject