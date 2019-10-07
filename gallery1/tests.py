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

