from django.contrib import admin
from django.contrib import messages
from django.db.models import Count, F, Sum, Max
import csv
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
from import_export.admin import ImportExportModelAdmin

from .models import Athlete, Country, City, Event, Result, Group, Distance, Team, Coach, BikeType

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

@admin.register(Athlete)
class AthleteAdmin(ImportExportModelAdmin, admin.ModelAdmin, ExportCsvMixin):
    list_display = ['id', 'first_name', 'last_name', 'nick_name', 'birth_date', 'city', 'gender', 'event_count', 'age', 'team', 'swim_coach', 'bike_coach', 'run_coach', 'triathlon_coach']
    list_filter = ('gender',)
    list_display_links = ['first_name']
    search_fields = ['first_name', 'last_name', 'nick_name']
    readonly_fields = ['headshot_image', 'age']

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.headshot.url,
            width=obj.headshot.width,
            height=obj.headshot.height,
            )
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _event_count=Count("event", distinct=True),
        )
        return queryset

    def event_count(self, obj):
        return obj.event.count()

    event_count.admin_order_field = '_event_count'

    actions = ["export_as_csv"]

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'city_count']
    list_filter = ('name',)
    search_fields = ['name']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _city_count=Count("city", distinct=True),
        )
        return queryset

    def city_count(self, obj):
        return obj.city.count()

    city_count.admin_order_field = '_city_count'

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'athlete_count']
    list_display_links = ['name']
    list_filter = ('city__name',)
    search_fields = ['name']

    def athlete_count(self, obj):
        return obj.athlete.count()

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(BikeType)
class BikeTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['name', 'country']
    list_filter = ('country__name',)
    search_fields = ['name']

    actions = ["export_as_csv"]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['name', 'event_date', 'city', 'athlete_count', 'swim', 'race_over']
    # list_filter = ('country',)
    search_fields = ['name', 'city']
    autocomplete_fields = ['city', 'athlete']

    date_hierarchy = 'event_date'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _athlete_count=Count("athlete", distinct=True),
        )
        return queryset

    def athlete_count(self, obj):
        return obj.athlete.count()

    athlete_count.admin_order_field = '_athlete_count'

    actions = ["export_as_csv"]

@admin.register(Result)
class ResultAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'athlete', 'event', 'group', 'distance', 'team', 'total_place', 'group_place', 'gender_place', 'bike_type', 'bike_model', 
    'total_swim_place', 'gender_swim_place', 'group_swim_place',
    'total_bike_place', 'total_place_after_bike', 'gender_bike_place', 'gender_place_after_bike', 'group_bike_place', 'group_place_after_bike',
    'total_run_place', 'gender_run_place', 'group_run_place',
    'run_shoes_model', 'swimming_time', 't1', 'biking_time', 't2', 'running_time', 'total_time', 'points']
    autocomplete_fields = ['event', 'athlete']
    list_filter = ['event',]
    # readonly_fields = ['total_time',]
    list_display_links = ['athlete']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            # _place=Max(F('swimming_time') + F('t1') + F('biking_time') + F('t2') + F('running_time')),
        )
        return queryset

    # def swim_time(self, obj):
    #     time = obj.swimming_time
    #     hours = int(time)
    #     minutes = (time*60) % 60
    #     seconds = (time*3600) % 60
    #     return "%d:%02d.%02d" % (hours, minutes, seconds)

    # swim_time.admin_order_field = '_swim_time'

    # def T1(self, obj):
    #     time = obj.transition1
    #     hours = int(time)
    #     minutes = (time*60) % 60
    #     seconds = (time*3600) % 60
    #     return "%d:%02d.%02d" % (hours, minutes, seconds)

    # T1.admin_order_field = '_T1'

    # def bike_time(self, obj):
    #     time = obj.biking_time
    #     hours = int(time)
    #     minutes = (time*60) % 60
    #     seconds = (time*3600) % 60
    #     return "%d:%02d.%02d" % (hours, minutes, seconds)

    # bike_time.admin_order_field = '_bike_time'

    # def T2(self, obj):
    #     time = obj.transition2
    #     hours = int(time)
    #     minutes = (time*60) % 60
    #     seconds = (time*3600) % 60
    #     return "%d:%02d.%02d" % (hours, minutes, seconds)

    # T2.admin_order_field = '_T2'

    # def run_time(self, obj):
    #     time = obj.running_time
    #     hours = int(time)
    #     minutes = (time*60) % 60
    #     seconds = (time*3600) % 60
    #     return "%d:%02d.%02d" % (hours, minutes, seconds)

    # run_time.admin_order_field = '_run_time'

    # def total_time(self, obj):
    #     time = obj.full_time#swimming_time + obj.transition1 + obj.biking_time + obj.transition2 + obj.running_time
    #     hours = int(time)
    #     minutes = (time*60) % 60
    #     seconds = (time*3600) % 60
    #     _total_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    #     return _total_time

    # total_time.admin_order_field = '_total_time'

    # def place(self, obj):
    #     return obj._place

    # place.admin_order_field = '_place'

class FirstLetterListFilter(admin.SimpleListFilter):
    title = 'Group'
    parameter_name = 'name'
    def lookups(self, request, model_admin):
        return (
            ('V', _('V')),
            ('M', _('M'))
        )
    def queryset(self, request, queryset):
        if self.value() in ('V', 'M'):
            return queryset.filter(name__istartswith=self.value())    
        elif self.value() == None:
            return queryset.filter(name__istartswith='')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = (FirstLetterListFilter,)
    search_fields = ['name']

@admin.register(Distance)
class DistanceAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ('name',)
    search_fields = ['name']
