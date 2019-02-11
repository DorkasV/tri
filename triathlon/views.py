from django.shortcuts import render
from triathlon.models import Athlete, Result, Event
from django.views import generic

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
