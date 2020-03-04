from django.test import TestCase
from phonebook_app.models import Contact
from rest_framework.test import APIRequestFactory
from phonebook_app.views import ContactViewSet


class ContactTestCase(TestCase):
    def setUp(self):
        Contact.objects.create(first_name="Richard", last_name="Platt", phone_number="123")
        Contact.objects.create(first_name="Suzie", last_name="Burns", phone_number="123")

    def test_contacts_are_contacts(self):
        richard = Contact.objects.get(first_name="Richard")
        suzie = Contact.objects.get(first_name="Suzie")
        self.assertTrue(isinstance(richard, Contact))
        self.assertTrue(isinstance(suzie, Contact))

    def test_post_contacts(self):
        factory = APIRequestFactory()
        data = {'first_name': 'Richard', 'last_name': 'Platt', 'phone_number': '123456'}
        request = factory.post('/contacts/', data)

        view = ContactViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, 201)



