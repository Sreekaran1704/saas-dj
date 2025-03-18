from django.db import models

# Create your models here.

class PageVisit(models.Model):
    # db -> Table
    # id -> Primary Key -> AutoField
    path = models.TextField(blank=True, null=True) #Column
    timestamp = models.DateTimeField(auto_now_add=True) #Column
