from django.test import TestCase
from .models import Menu, Item, Person, Adhar, Movie, Artists


class MenuModelTest(TestCase):
    """Test cases for Menu model"""

    def setUp(self):
        self.menu = Menu.objects.create(name='Test Menu')

    def test_menu_creation(self):
        """Test menu is created correctly"""
        self.assertEqual(self.menu.name, 'Test Menu')
        self.assertEqual(str(self.menu), 'Test Menu')


class ItemModelTest(TestCase):
    """Test cases for Item model (One-to-Many relationship)"""

    def setUp(self):
        self.menu = Menu.objects.create(name='Test Menu')
        self.item = Item.objects.create(
            menu=self.menu,
            name='Test Item',
            description='Test Description'
        )

    def test_item_creation(self):
        """Test item is created correctly"""
        self.assertEqual(self.item.name, 'Test Item')
        self.assertEqual(self.item.description, 'Test Description')
        self.assertEqual(str(self.item), 'Test Item')

    def test_item_menu_relationship(self):
        """Test one-to-many relationship between Menu and Item"""
        self.assertEqual(self.item.menu, self.menu)
        self.assertIn(self.item, self.menu.item_set.all())

    def test_cascade_delete(self):
        """Test cascade delete when menu is deleted"""
        menu_id = self.menu.id
        item_id = self.item.id
        self.menu.delete()
        self.assertFalse(Item.objects.filter(id=item_id).exists())


class PersonAdharModelTest(TestCase):
    """Test cases for Person and Adhar models (One-to-One relationship)"""

    def setUp(self):
        self.person = Person.objects.create(
            name='John Doe',
            email='john@example.com',
            mobile='1234567890'
        )
        self.adhar = Adhar.objects.create(
            person=self.person,
            signature='John Signature',
            adhar_no='123456789012'
        )

    def test_person_creation(self):
        """Test person is created correctly"""
        self.assertEqual(self.person.name, 'John Doe')
        self.assertEqual(self.person.email, 'john@example.com')
        self.assertEqual(self.person.mobile, '1234567890')

    def test_adhar_creation(self):
        """Test adhar is created correctly"""
        self.assertEqual(self.adhar.signature, 'John Signature')
        self.assertEqual(self.adhar.adhar_no, '123456789012')

    def test_one_to_one_relationship(self):
        """Test one-to-one relationship between Person and Adhar"""
        self.assertEqual(self.adhar.person, self.person)
        self.assertEqual(self.person.adhar, self.adhar)

    def test_cascade_delete_adhar(self):
        """Test cascade delete when person is deleted"""
        person_id = self.person.id
        adhar_id = self.adhar.id
        self.person.delete()
        self.assertFalse(Adhar.objects.filter(id=adhar_id).exists())


class MovieArtistsModelTest(TestCase):
    """Test cases for Movie and Artists models (Many-to-Many relationship)"""

    def setUp(self):
        self.movie1 = Movie.objects.create(name='Movie 1')
        self.movie2 = Movie.objects.create(name='Movie 2')
        self.artist = Artists.objects.create(name='Artist 1')
        self.artist.movies.add(self.movie1, self.movie2)

    def test_movie_creation(self):
        """Test movie is created correctly"""
        self.assertEqual(self.movie1.name, 'Movie 1')
        self.assertEqual(str(self.movie1), 'Movie 1')

    def test_artist_creation(self):
        """Test artist is created correctly"""
        self.assertEqual(self.artist.name, 'Artist 1')

    def test_many_to_many_relationship(self):
        """Test many-to-many relationship between Movie and Artists"""
        self.assertIn(self.movie1, self.artist.movies.all())
        self.assertIn(self.movie2, self.artist.movies.all())
        self.assertEqual(self.artist.movies.count(), 2)

    def test_reverse_many_to_many(self):
        """Test reverse many-to-many relationship"""
        self.assertIn(self.artist, self.movie1.artists_set.all())
        self.assertIn(self.artist, self.movie2.artists_set.all())

    def test_remove_movie_from_artist(self):
        """Test removing movie from artist"""
        self.artist.movies.remove(self.movie1)
        self.assertNotIn(self.movie1, self.artist.movies.all())
        self.assertIn(self.movie2, self.artist.movies.all())
