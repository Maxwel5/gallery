from django.test import TestCase
from .models import Photo,categories,location

# Create your tests here.
class PhotoTestCase(TestCase):
    # Set Up method
    def setUp(self):
        self.food= Photo(name='food',description='The essential requirement for human body to aid in growth and development'image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQw55lGYQ63etgGDG2vcDjOdGEFgoUrNz5h9Qu9bO9_EOq9Vx9M')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.photo,Photo))

    def test_save_method(self):
        self.photo.save_photo()
        photo = Photo.objects.all()
        self.assertTrue(len(photo) > 0)

    def test_delete_photo(self):
        self.photo.save_photo()
        self.searched_photo = Photo.get_photo_by_id(1)
        self.searched_photo.delete_photo()
        self.assertTrue(len(Photo.objects.all()) == 0)
    
    def test_display_method(self):
        self.photo.save_photo()
        self.photo = Photo.objects.filter(id=1).display(photo_url = '/photo')
        self.display_photo = Photo.get_photo_by_id(1)
        self.assertTrue(self.display_photo.photo_url,"/photo")

    def test_update_photo(self):
        self.photo.save_photo()
        self.photo = Photo.objects.filter(id = 1).update(photo_url = "/photo")
        self.updated_photo = Photo.get_photo_by_id(1)
        self.assertEqual(self.updated_photo.photo_url,"/photo")

