from rest_framework import serializers
from note.models import Note

class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields =(
            'id',
            'title',
            'text',
            'create_date',
            'update_date'

        )