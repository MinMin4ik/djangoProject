from django.test import TestCase
from food_shop.models import Category, Company


# from food_shop.models import company


class Company:
    pass


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

    def test_update_Company(self):
        new_title = 'new test title'
        payload = {
            'title': 'test_title',
        }
        Company = Company.objects
        Company.title = new_title
        Company.save()
        Company.refresh_from_db()
        self.assertEqual(Company.title, new_title)

    def test_update_company_fail(self):
        payload = {
            'title': 'new test title',
            'unknown_field': 'value'
        }
        with self.assertRaises(TypeError):
            Company.refresh_from_db

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
            category = Category.objects.get(pk=pk)
