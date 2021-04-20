from django.test import TestCase

from food_shop.forms import SearchForm

class SearchFormTest(TestCase):
    def test_search_success(self):
        form_data =  {
            'search_string'
        }