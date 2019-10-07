from django.db import models

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # location = models.ForeignKey(Location,on_delete=models.CASCADE) 
    # category = models.ManyToManyField(categories)
    image_url = models.ImageField(upload_to="user_images/%Y/%m/%d/")
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()
