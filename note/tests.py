from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from note.models import Note
from .serializers import NoteSerializers

class createNote(APITestCase):
    def setUp(self):
        self.data = {'title':'Test Note',
        'text':'Test Note '}

    def test_create_note(self):
        response = self.client.post(reverse('NoteList'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadNote(APITestCase):
    def setUp(self):
        self.data = {'title':'Test Note',
        'text':'Test Note '}

        self.note = Note.objects.create(title = 'Test Note',
        text = 'Test Note')

    def test_read_note_list(self):
        response = self.client.get(reverse('NoteList'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_note_detail(self):
        response = self.client.get(reverse('NoteDetail', args=[self.note.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateNote(APITestCase):
    def setUp(self):
        self.note = Note.objects.create(title = 'Test Note',
        text = 'Test Note')

        self.data = NoteSerializers(self.note).data
        self.data.update({'title' : 'Updated Title'})


    def test_update_note(self):
        response = self.client.put(reverse('NoteDetail', args=[self.note.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class DeleteNote(APITestCase):
    def setUp(self):
        self.note = Note.objects.create(title = 'Test Note',
        text = 'Test Note')

    def test_delete_note(self):
        response = self.client.delete(reverse('NoteDetail', args=[self.note.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class PatchNote(APITestCase):
    def setUp(self):
        self.note = Note.objects.create(title = 'Test Note',
        text = 'Test Note')

        self.data = NoteSerializers(self.note).data
        self.data.update({'title' : 'Updated Title'})

    def test_patch_note(self):
        response = self.client.patch(reverse('NoteDetail', args=[self.note.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
