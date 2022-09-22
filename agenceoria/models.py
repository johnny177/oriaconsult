from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
# Create your models here.
"""
class trip(models.Model):
     id_trip=models.AutoField(primary_key=True)
     name= models.CharField(max_length=25)
     date_depart=models.DateTimeField()
     date_arrive=models.DateTimeField()
     price=models.FloatField()
     
class booking(models.Model):
     id_booking=models.AutoField(primary_key=True)
     origin= models.CharField(max_length=25)
     destination=models.DateTimeField()
     date_depart=models.DateTimeField()
     date_arrive=models.DateTimeField()
     Class=models.CharField(max_length=25)
    
class Services(models.Model):
    class Meta:
        abstract = True
class travelling(Services):
    class Meta:
        abstract = True
class educational(Services):
    class Meta:
        abstract = True
class visa(Services):
    class Meta:
        abstract = True
class others(Services):
    class Meta:
        abstract = True
 """
class Gallery(models.Model):
     id_Gallery=models.AutoField(primary_key=True)
     Picture=models.ImageField()
     tag= models.CharField(max_length=25)
"""class Feedback(models.Model): 
      id_Feedback=models.AutoField(primary_key=True) 
      Picture = models.ForeignKey("Gallery", on_delete=models.CASCADE)
      comment = models.TextField()      
class BookingInformation(models.Model):
    id_BookingInformation=models.AutoField(primary_key=True)
class countries(models.Model):
    id_countries=models.AutoField(primary_key=True)
    name= models.CharField(max_length=25)
class regions(models.Model):
    id_regions=models.AutoField(primary_key=True)
    name= models.CharField(max_length=25)
class local(travelling):
    id_local=models.AutoField(primary_key=True)
class international(travelling):
    id_international=models.AutoField(primary_key=True)
class GeneralTravelConsultancy(travelling):
    id_GeneralTravelConsultancy=models.AutoField(primary_key=True)
class FlightTicket(travelling):
    id_FlightTicket=models.AutoField(primary_key=True)    

class StudyAbroad(models.Model):
    id_StudyAbroad=models.AutoField(primary_key=True)
class IELTS(models.Model):
    id_IELTS=models.AutoField(primary_key=True)
class Scholarship(models.Model):
    id_Scholarship=models.AutoField(primary_key=True)"""
class CVResume(models.Model):
    id_CVResume=models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    Telephone = models.CharField(max_length=20,blank=True, null=True)
    Email  = models.EmailField(max_length=45, blank=True, null=True)
    Career_objective = models.TextField(null=True)
    Year_admission_university = models.CharField(max_length=4,blank=True, null=True)
    courses = models.TextField(null=True)
    experiences = models.TextField(null=True)
    activities = models.TextField(null=True)
    skills = models.TextField(null=True)
    witnesses = models.TextField(null=True)
    #cv=models.FileField(upload_to='cv')
"""class HotelBooking(models.Model):
    id_HotelBooking=models.AutoField(primary_key=True)
class StudentProfile(models.Model):
    id_StudentProfile=models.AutoField(primary_key=True)
class InterviewTraining(models.Model):
    id_InterviewTraining=models.AutoField(primary_key=True)
class Hotel(models.Model):
    id_Hotel=models.AutoField(primary_key=True)
    name= models.CharField(max_length=25)
    region= models.ForeignKey("Place", on_delete=models.CASCADE)"""
class Universities(models.Model):
    id_Universities=models.AutoField(primary_key=True)
    name= models.CharField(max_length=25)
    country= models.ForeignKey("Place", on_delete=models.CASCADE)
    
    
typevisa = (('1','Student Visa'), 
        ('2','Short term Visa'),
        ('3','UK Settlement application'))
class visa(models.Model):
   id_visa=models.AutoField(primary_key=True)
   user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
   Name=models.CharField(max_length=25)
   Contact=models.CharField(max_length=25)
   Type= models.CharField(max_length=20, choices=typevisa)
types = (('1','Universities Application/Admission'), 
        ('2','Admission Documents review'),
        ('3','Funding Assistance (Discounts, Scholarships, Teaching/Assistantships, & Loans)'),
        ('4','IELTS Tests'))
hows = (('1','By email'), 
        ('2','By phone'))        
class studyserv(models.Model):
   id_studyserv=models.AutoField(primary_key=True)
   user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
   Name=models.CharField(max_length=25)
   Contact=models.CharField(max_length=25) 
   Email=models.EmailField()
   ServiceType= models.CharField(max_length=20, choices=types, null=True)
   How= models.CharField(max_length=20, choices=hows, null=True)
class Courses(models.Model):
   topic=models.CharField(max_length=250)
   description=models.TextField()
   country=models.CharField(max_length=25)
   city=models.CharField(max_length=25)
   date = models.DateField(blank=True)
   datetime = models.TimeField(auto_now=False, auto_now_add=False)
   duration=models.CharField(max_length=50)
   def __str__(self):
        return f"{self.topic}, {self.date} in {self.country}"
class Coursespart(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
   course = models.ForeignKey(Courses, on_delete=models.CASCADE, blank=True, null=True)
   Name=models.CharField(max_length=25)
   Contact=models.CharField(max_length=25) 
   Email=models.EmailField()  

class Events(models.Model):
   topic=models.CharField(max_length=250)
   description=models.TextField()
   country=models.CharField(max_length=25)
   city=models.CharField(max_length=25)
   date = models.DateField(blank=True)
   datetime = models.TimeField(auto_now=False, auto_now_add=False)
class Eventspart(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
   Event = models.ForeignKey(Events, on_delete=models.CASCADE, blank=True, null=True)
   Name=models.CharField(max_length=25)
   Contact=models.CharField(max_length=25) 
   Email=models.EmailField()  
  
####################################################################""
TYPEPLACE = (('local','LOCAL'), 
    ('international','INTERNATIONAL'))
class Place(models.Model):
    city = models.CharField(max_length=64)
    airport = models.CharField(max_length=64)
    code = models.CharField(max_length=3)
    country = models.CharField(max_length=64)
    typep = models.CharField(max_length=20, choices=TYPEPLACE, blank=True)
    def __str__(self):
        return f"{self.city}, {self.country} ({self.code})"

"""
class Week(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name} ({self.number})"
"""
week = (('1','saturday'), 
        ('2','sunday'),
        ('3','monday'),  
        ('4','tuesday'),
        ('5','wednesday'),
        ('6','thursday'),    
        ('7','friday'))

class Flight(models.Model):
    origin = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="arrivals", null=True)
    depart_time = models.TimeField(auto_now=False, auto_now_add=False)
    depart_day = models.DateField(blank=True)
    #duration = models.DurationField(null=True)
    arrival_time = models.TimeField(auto_now=False, auto_now_add=False)
    #plane = models.CharField(max_length=24)
    #airline = models.CharField(max_length=64)
    #economy_fare = models.FloatField(null=True)
    #business_fare = models.FloatField(null=True)
    #first_fare = models.FloatField(null=True)
    fare=models.FloatField(null=True)
    max_booking = models.IntegerField(null=True)
    number_booking = models.IntegerField(null=True)
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

GENDER = (
    ('male','MALE'),    #(actual_value, human_readable_value)
    ('female','FEMALE')
)

class Passenger(models.Model):
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, blank=True)
    #passenger = models.ForeignKey(User, on_delete=models.CASCADE, related_name="flights")
    #flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="passengers")

    def __str__(self):
        return f"Passenger: {self.first_name} {self.last_name}, {self.gender}"



SEAT_CLASS = (
    ('economy', 'Economy'),
    ('business', 'Business'),
    ('first', 'First')
)

TICKET_STATUS =(
    ('PENDING', 'Pending'),
    ('CONFIRMED', 'Confirmed'),
    ('CANCELLED', 'Cancelled')
)

class Ticket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="bookings", blank=True, null=True)
    ref_no = models.CharField(max_length=6, unique=True)
    passengers = models.ForeignKey(Passenger, related_name="flight_tickets",on_delete=models.CASCADE, blank=True, null=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="tickets", blank=True, null=True)
    flight_ddate = models.DateField(blank=True, null=True)
    flight_adate = models.DateField(blank=True, null=True)
    flight_fare = models.FloatField(blank=True,null=True)
    #other_charges = models.FloatField(blank=True,null=True)
    #coupon_used = models.CharField(max_length=15,blank=True)
    #coupon_discount = models.FloatField(default=0.0)
    total_fare = models.FloatField(blank=True, null=True)
    #seat_class = models.CharField(max_length=20, choices=SEAT_CLASS)
    booking_date = models.DateTimeField(default=datetime.now)
    mobile = models.CharField(max_length=20,blank=True)
    email = models.EmailField(max_length=45, blank=True)
    status = models.CharField(max_length=45, choices=TICKET_STATUS)

    def __str__(self):
        return self.ref_no