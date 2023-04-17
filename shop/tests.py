from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from .models import Products, Order

# Create your tests here.
class ShopTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.product1 = Products.objects.create(title='Product 1', price=10.0,
                                                discount_price=8.0, 
                                                category='Category 1', 
                                                description='Description 1', 
                                                image='Image 1')
        self.product2 = Products.objects.create(title='Product 2', price=20.0, 
                                                discount_price=15.0, 
                                                category='Category 2', 
                                                description='Description 2', 
                                                image='Image 2')
        self.order = Order.objects.create(items='Product 1, Product 2', 
                                          name='Test Name', 
                                          email='test@example.com', 
                                          address='123 Test Street', 
                                          city='Test City', 
                                          state='Test State', 
                                          zipcode='12345', 
                                          total='23.0')

    def test_index_view(self):
        """
        Test that the index view returns the correct status code and
        that the context contains the expected keys and values.
        """
        response = self.client.get(reverse('shop:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.title)
        self.assertContains(response, self.product2.title)

    def test_search_view(self):
        """
        Test that the search view returns the correct status code and 
        that the context contains the expected keys and values.
        """
        response = self.client.get(reverse('shop:index'), {'item_name': 'Product 1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.title)
        self.assertNotContains(response, self.product2.title)

    def test_detail_view(self):
        """
        Test that the detail view returns the correct status code and 
        that the context contains the expected keys and values.
        """
        response = self.client.get(reverse('shop:detail', args=[self.product1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.title)

    def test_checkout_view(self):
        """
        Test that the checkout view returns the correct status code and 
        that the template used is correct.
        """
        response = self.client.post(reverse('shop:checkout'), \
                                    {'items': 'Product 1, Product 2', 
                                     'name': 'Test Name', 
                                     'email': 'test@example.com', 
                                     'address': '123 Test Street', 
                                     'city': 'Test City', 
                                     'state': 'Test State', 
                                     'zipcode': '12345', 
                                     'total': '23.0'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/checkout.html')
        self.assertEqual(Order.objects.count(), 2)
