from rest_framework import serializers
from .models import *



class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField( read_only=True)
    class Meta:
        model = Note
        fields = '__all__'







