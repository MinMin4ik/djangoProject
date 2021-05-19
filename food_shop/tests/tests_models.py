from django.test import TestCase
from food_shop.models import Category


class TestCategory(TestCase):
    def test_create_category_success(self):
        payload = {
            'title': 'test_title'
        }
        category = Category.objects.create(**payload)
        self.assertEqual(category.title, payload['title'])

    def test_create_category_fail(self):
        payload = {
            'title': 'test_title',
            'unknown_field': 'value'
        }
        with self.assertRaises(TypeError):
            Category.objects.create(**payload)

    """
    Testing model updating function.
    """

    def test_update_category_success(self):
        new_title = 'new test title'
        payload = {
            'title': 'test_title',
        }
        category = Category.objects.create(**payload)
        category.title = new_title
        category.save()
        category.refresh_from_db()
        self.assertEqual(category.title, new_title)

    def test_update_category_fail(self):
        """new test title"""
        payload = {
            'title': 'test_title',
        }
        category = Category.objects.create(**payload)
        category.title = 1
        category.save()
        category_from_db = Category.objects.get(id=category.id)
        print(category.__dict__)
        self.assertNotEqual(category.__dict__, category_from_db.__dict__)

    """
    Testing model deleting function.
    """

    def test_delete_category(self):
        payload = {
            'title': 'test_title',
        }
        category = Category.objects.create(**payload)
        pk = category.pk
        category.delete()
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(pk=pk)


class TestDish(TestCase):
    def test_create_dish_success(self):
        payload = {
            'title': 'mi note 10',
            'description': '',
            'category': 1,
            'company': 1,
            'image': ''

        }

    """
    Testing model deleting function.
    """

# class Directory_Tests(TestCase):
#     def test_directory_success200(self):
#         payload = {
#         ""
#         }

