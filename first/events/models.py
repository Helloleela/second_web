from re import L
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Venue(models.Model):
    name = models.CharField("Venue Name", max_length=100)
    address =models.CharField(max_length=200)
    zip_code = models.CharField("Zip Code", max_length=6)
    phone = models.CharField("Contact Phone", max_length=10, blank=True)
    web = models.URLField("Website Address", blank=True)
    email_address = models.EmailField("Email Address", blank=True)

    def __str__(self):
        return self.name    


class ClubUser(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField("User Email")

    def __str__(self):
        return self.first_name + " "+self.last_name       

class Event(models.Model):
    name = models.CharField("Event Name", max_length=100)
    event_date = models.DateTimeField("Event Date")
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager =models.ForeignKey(User, blank=True,null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(ClubUser, blank=True)


    def __str__(self):
        return self.name


