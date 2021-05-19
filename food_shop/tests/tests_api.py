from django.urls import reverse
from rest_framework import status
import food_shop


def test_post_logged_in(self):
    product = food_shop.objects.get(id=1)
    self.client.login(username='test', password='123')
    data = {
        'nick': self.user.id,
        'rate': '1/5',
        'content': 'here is comment',
        'product': product.id
    }
    response = self.client.post(reverse('add_comments', kwargs={'id': product.id}), data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK,
                     f'expected Response code 201, instead get'
                     f'{response.status_code}')
