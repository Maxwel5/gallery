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
    # category_photo = models.PhotoField(upload_to = 'categories/')

    def __str__(self):
        return self.name

    def save_categories(self):
        self.save() 

    def delete_categories(self):
        self.delete() 

class Photo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(location) 
    category = models.ManyToManyField(categories)
    image_url = models.ImageField(upload_to="user_images/")
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.delete()

    @classmethod
    def create_album(cls):
        gallery1 = cls.objects.all()
        return gallery1

    # @classmethod
    # def display_gallery1(cls,photo):
    #     gallery1 = cls.objects.filter(category__name__icontains = display_gallery1)
    #     return gallery1

    @classmethod
    def search_by_category(cls,search_term):
        gallery1 = cls.objects.filter(category__name__icontains=search_term)
        return gallery1
