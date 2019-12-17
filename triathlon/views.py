from django.shortcuts import render
from triathlon.models import Athlete, Result, Event, Distance, Group, Country, City, Team
from django.views import generic
from .serializers import AthleteSerializer, EventSerializer, ResultSerializer, DistanceSerializer, GroupSerializer, CountrySerializer, CitySerializer, TeamSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import pagination, response

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

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'per_page'
    max_page_size = 1000

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'per_page'
    # max_page_size = 100

    # Paginate in the style defined by vuetable2
    def get_paginated_response(self, data):

        # Get id's of records in current page
        firstRecord = data[0]['id'] if (data and 'id' in data[0]) else None
        lastRecord = data[-1]['id'] if (data and 'id' in data[0]) else None

        return response.Response({
            'pagination': {
                'total': self.page.paginator.count,
                'per_page': self.get_page_size(self.request),
                'current_page': self.request.query_params.get('page', None),
                'last_page': self.page.paginator.num_pages,
                'next_page_url': self.get_next_link(),
                'previous_page_url': self.get_previous_link(),
                "from": firstRecord,
                "to": lastRecord,
            },
            'data': data
        })

class AthleteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows athletes to be viewed or edited.
    """
    queryset = Athlete.objects.all().order_by('pk')
    serializer_class = AthleteSerializer
    pagination_class = CustomPagination

    search_fields = ['first_name', 'last_name']
    filterset_fields = [
        'event', 'team'
    ]

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('pk')
    serializer_class = EventSerializer
    pagination_class = CustomPagination

    search_fields = ['name']
    filterset_fields = [
        'athlete',
    ]

class ResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows results to be viewed or edited.
    """
    queryset = Result.objects.all().order_by('-event__event_date')
    serializer_class = ResultSerializer
    pagination_class = CustomPagination

    search_fields = ['event__name', 'athlete__first_name', 'athlete__last_name', 'team__name']
    filterset_fields = [
        'event', 'athlete', 'team', 'distance'
    ]

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

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Team.objects.all().order_by('pk')
    serializer_class = TeamSerializer
    pagination_class = CustomPagination

    search_fields = ['name']
    filterset_fields = [
        'athlete',
    ]
