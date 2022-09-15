from django.db import models

# Create your models here.

class seller(models.Model):
    sell_Id = models.IntegerField()
    sell_name = models.CharField(max_length = 255)
    sell_gender = models.CharField(max_length = 255)
    sell_Address = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.sell_name

class store(models.Model):
    
    st_name = models.CharField(max_length = 255)
    st_location = models.CharField(max_length = 255)
    st_Address = models.CharField(max_length = 255)
    st_status = models.BooleanField()
    seller = models.ForeignKey(seller, on_delete = models.CASCADE)
    image = models.FileField(upload_to="blog/app/media/store", null=True, blank=True)
    def __str__(self):
        return self.st_name

