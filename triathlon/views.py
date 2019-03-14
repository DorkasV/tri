from django.shortcuts import render
from triathlon.models import Athlete, Result, Event, Distance, Group, Country, City
from django.views import generic
from .serializers import AthleteSerializer, EventSerializer, ResultSerializer, DistanceSerializer, GroupSerializer, CountrySerializer, CitySerializer
from rest_framework import viewsets

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_athletes = Athlete.objects.all().count()
    num_results = Result.objects.all().count()
    # num_events = Event.objects.all().count()
    
    # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_events = Event.objects.count()
    
    context = {
        'num_athletes': num_athletes,
        'num_results': num_results,
        # 'num_instances_available': num_instances_available,
        'num_events': num_events,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class AthleteListView(generic.ListView):
    model = Athlete
    paginate_by = 10

class AthleteDetailView(generic.DetailView):
    model = Athlete
    paginate_by = 10

class EventListView(generic.ListView):
    model = Event
    paginate_by = 10

class EventDetailView(generic.DetailView):
    model = Event
    paginate_by = 10

class ResultListView(generic.ListView):
    model = Result
    paginate_by = 10

class ResultDetailView(generic.DetailView):
    model = Result
    paginate_by = 10

class AthleteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows athletes to be viewed or edited.
    """
    queryset = Athlete.objects.all().order_by('-pk')
    serializer_class = AthleteSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-pk')
    serializer_class = EventSerializer

class ResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows results to be viewed or edited.
    """
    queryset = Result.objects.all().order_by('-pk')
    serializer_class = ResultSerializer

class DistanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows distances to be viewed or edited.
    """
    queryset = Distance.objects.all().order_by('-pk')
    serializer_class = DistanceSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('-pk')
    serializer_class = GroupSerializer

class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows countries to be viewed or edited.
    """
    queryset = Country.objects.all().order_by('-pk')
    serializer_class = CountrySerializer

class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cities to be viewed or edited.
    """
    queryset = City.objects.all().order_by('-pk')
    serializer_class = CitySerializer
