from rest_framework import viewsets
from phonebook_app.models import Contact
from phonebook_app.serializer import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

