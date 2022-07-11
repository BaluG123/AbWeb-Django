from pyexpat import model
from rest_framework import serializers
from testapp.models import Sports,Entertainment,Technology,EditorChoice

class SportsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Sports
        fields='__all__'

class EntertainmentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Entertainment
        fields='__all__'

class TechnologySerializers(serializers.ModelSerializer):
    class Meta:
        model=Technology
        fields='__all__'

class EditorSerializers(serializers.ModelSerializer):
    class Meta:
        model=EditorChoice
        fields='__all__'