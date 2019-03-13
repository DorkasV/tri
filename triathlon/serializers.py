from rest_framework import serializers
from .models import Athlete, Event, Result, Distance, Group, Country, City

class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Athlete
        fields = ('first_name', 'last_name', 'birth_date', 'age', 'gender')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'city')

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = ('event', 'athlete', 'distance', 'group', 'swimming_time', 't1', 'biking_time', 't2', 'running_time')

class DistanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distance
        fields = ('name',)

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('name', 'country')
