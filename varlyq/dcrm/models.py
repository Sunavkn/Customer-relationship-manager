from django.db import models

class Record(models.Model):
    creation_date=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    postcode=models.CharField(max_length=8)
    sequence_id = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.first_name+"   "+self.last_name