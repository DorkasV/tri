from django.db import models
from django.urls import reverse
from dateutil.relativedelta import relativedelta
from datetime import datetime, date
from django.utils import timezone

class Distance(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Cities'

    country = models.ForeignKey(
        Country,
        related_name='city',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return "%s, %s" % (self.name, self.country)

class Athlete(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField('birth date')
    age = models.IntegerField(null=True, blank=True,)
    
    MALE = 'M'
    FEMALE = 'F'
    CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(
        max_length=1,
        choices=CHOICES,
        default=MALE,
    )

    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
    )

    headshot = models.ImageField(null=True, blank=True, upload_to="athlete_headshots/")

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('athlete-detail', args=[str(self.id)])

    def get_age(self):
        return relativedelta(datetime.now(), self.birth_date).years

    class Meta:
        ordering = ['last_name']

    def save(self, *args, **kwargs):
        self.age = self.get_age()
        super(Athlete, self).save(*args, **kwargs)

class Event(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateField('event date')

    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    athlete = models.ManyToManyField(Athlete, related_name='event', blank=True)

    def race_over(self):
        now = datetime(timezone.now().year, timezone.now().month, timezone.now().day)
        d = self.event_date
        dt = datetime(d.year, d.month, d.day)
        return now <= dt <= now
    race_over.admin_order_field = 'event_date'
    race_over.boolean = True
    race_over.short_description = 'Race over?'

    def __str__(self):
        return "%s %s" % (self.name, self.city)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('event-detail', args=[str(self.id)])

    class Meta:
        ordering = ['event_date']

class Result(models.Model):
    event = models.ForeignKey(
        Event,
        related_name='result',
        on_delete=models.CASCADE,
        null=True,
    )

    athlete = models.ForeignKey(
        Athlete,
        related_name='result',
        on_delete=models.CASCADE,
        null=True,
    )

    distance = models.ForeignKey(
        Distance,
        on_delete=models.CASCADE,
        null=True,
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
    )

    total_place = models.CharField(max_length=10, blank=True)
    gender_place = models.CharField(max_length=10, blank=True)
    group_place = models.CharField(max_length=10, blank=True)

    swimming_time = models.DurationField(blank=True, null=True)
    t1 = models.DurationField(blank=True, null=True)
    biking_time = models.DurationField(blank=True, null=True)
    t2 = models.DurationField(blank=True, null=True)
    running_time = models.DurationField(blank=True, null=True)
    total_time = models.DurationField(blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.athlete, self.event)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('result-detail', args=[str(self.id)])

    def get_total_time(self):
        "Returns total time."
        return self.swimming_time + self.t1 + self.biking_time + self.t2 + self.running_time

    def save(self, *args, **kwargs):
        self.total_time = self.get_total_time()
        super(Result, self).save(*args, **kwargs)
