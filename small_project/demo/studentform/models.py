from django.db import models

# Create your models here.

class studentform(models.Model):
    student_name = models.CharField(max_length=20, null=False, blank=True)
    Email_id = models.EmailField(max_length=30, null=True)
    contact_number = models.IntegerField(null=True)
    Address = models.CharField(max_length=50, null=True)
    
