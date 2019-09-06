from rest_framework import serializers
from .models import Athlete, Event, Result, Distance, Group, Country, City, Team

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)

class CitySerializer(serializers.HyperlinkedModelSerializer):
    country = CountrySerializer(read_only = True)
    class Meta:
        model = City
        fields = ('name', 'country')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    city = CitySerializer(read_only = True)
    class Meta:
        model = Team
        fields = ('id', 'name', 'city', 'athlete') 

class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    team = TeamSerializer(read_only = True)
    city = CitySerializer(read_only = True)
    class Meta:
        model = Athlete
        fields = ('id', 'first_name', 'last_name', 'birth_date', 'age', 'gender', 'city', 'team')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    city = CitySerializer(read_only = True)
    class Meta:
        model = Event
        fields = ('id', 'url', 'city', 'name', 'event_date', 'swim', 'athlete')

class DistanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distance
        fields = ('id', 'name',)

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    event = EventSerializer(read_only = True)
    athlete = AthleteSerializer(read_only = True)
    distance = DistanceSerializer(read_only = True)
    group = GroupSerializer(read_only = True)
    team = TeamSerializer(read_only = True)
    class Meta:
        model = Result
        fields = ('id', 'event', 'athlete', 'distance', 'group', 'swimming_time', 't1', 'biking_time', 't2', 'running_time', 'team', 'total_time', 'total_place', 'group_place', 'gender_place')
