from . serializers import EditorSerializers, EntertainmentSerializers, SportsSerializers, TechnologySerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from testapp.models import Sports,Entertainment,Technology,EditorChoice

class Sports_view(ModelViewSet):
    queryset=Sports.objects.all()
    serializer_class=SportsSerializers

class Tech_view(ModelViewSet):
    queryset=Technology.objects.all()
    serializer_class=TechnologySerializers

class Entertainment_view(ModelViewSet):
    queryset=Entertainment.objects.all()
    serializer_class=EntertainmentSerializers

class Editorchoice_view(ModelViewSet):
    queryset=EditorChoice.objects.all()
    serializer_class=EditorSerializers    
