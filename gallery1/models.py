from django.db import models

# Create your models here.

class location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save() 

    def delete_location(self):
        self.delete() 

class categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save_categories(self):
        self.save() 

    def delete_categories(self):
        self.delete() 

class Photo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(location,on_delete=models.CASCADE) 
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
