from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .models import *
import math
from datetime import datetime
from django.contrib.auth import authenticate, login, logout

from .constant import FEE
from oria.utils import createticket,createvisa,createcoursespart



from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

"""try:
    if len(Week.objects.all()) == 0:
        createWeekDays()
       
    if len(Place.objects.all()) == 0:
        addPlaces()
   

    if len(Flight.objects.all()) == 0:
        print("Do you want to add flights in the Database? (y/n)")
        if input().lower() in ['y', 'yes']:
            addDomesticFlights()
            addInternationalFlights()
except:
    pass""" 
# Create your views here.
def home(request):     
    return render(request,"admin/home.html", locals())
def index(request):
    Evenements=Events.objects.all()
    if request.method == "POST":       
        courseI= request.POST.get('courseId')
        course1 = Events.objects.get(id=courseI)
        return render(request, "admin/index1.html", locals(),{'course1':course1,
        'courseId':courseI})
    else:
        return render(request,  'admin/index1.html', locals())
    #return render(request, 'admin/index1.html', locals())
def eventpar(request):
 courseIDD = request.GET.get('courseId')
 if request.method == "POST":
    if request.user.is_authenticated:
        coursee = request.POST['courseI']
        cc = Events.objects.get(id=coursee)
        name1 = request.POST['name']
        contact1 = request.POST['contact']
        email1 = request.POST["email"]            
        try:  
           cp = Eventspart.objects.create()
           cp.user = request.user
           cp.Event=cc
           cp.Name= name1
           cp.Contact=contact1
           cp.Email=email1
           cp.save()           
        except Exception as e:
                return HttpResponse(e)
        return render(request, "admin/eventpar.html", { "message": " Your forum is successfully filled ✓ you can not register again !",'courseI':courseIDD,
        'cc':cc})
    else:
            return HttpResponseRedirect(reverse("login"))
 else:
        course1 = Events.objects.get(id=courseIDD)
        return render(request, 'admin/eventpar.html',{'courseI':courseIDD,
        'course1':course1})
    #return render(request, 'admin/eventpar.html', locals())
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
            
        else:
            return render(request, "admin/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "admin/login.html")

def register_view(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST["username"]
        email = request.POST["email"]
        contact=request.POST["contact"]
        TC=request.POST["TC"]
        # Ensuring password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "admin/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save()
        except:
            return render(request, "admin/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "admin/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def international(request):
    p=Place.objects.all()
    min_date = f"{datetime.now().date().year}-{datetime.now().date().month}-{datetime.now().date().day}"
    max_date = f"{datetime.now().date().year if (datetime.now().date().month+3)<=12 else datetime.now().date().year+1}-{(datetime.now().date().month + 3) if (datetime.now().date().month+3)<=12 else (datetime.now().date().month+3-12)}-{datetime.now().date().day}"
    if request.method == 'POST':
        origin = request.POST.get('Origin')
        destination = request.POST.get('Destination')
        depart_date = request.POST.get('DepartDate')
        #seat = request.POST.get('SeatClass')
        trip_type = request.POST.get('TripType')
        if(trip_type == '1'):
            return render(request, 'admin/international.html', locals(), {
            'origin': origin,
            'destination': destination,
            'depart_date': depart_date,
            #'seat': seat.lower(),
            'trip_type': trip_type
        })
        elif(trip_type == '2'):
            return_date = request.POST.get('ReturnDate')
            return render(request, 'admin/international.html', locals(), {
            'min_date': min_date,
            'max_date': max_date,
            'origin': origin,
            'destination': destination,
            'depart_date': depart_date,
            #'seat': seat.lower(),
            'trip_type': trip_type,
            'return_date': return_date
        })
    else:
        return render(request, 'admin/international.html', locals(), {
            'min_date': min_date,
            'max_date': max_date
        })
        
def local(request):
    p=Place.objects.all()
    min_date = f"{datetime.now().date().year}-{datetime.now().date().month}-{datetime.now().date().day}"
    max_date = f"{datetime.now().date().year if (datetime.now().date().month+3)<=12 else datetime.now().date().year+1}-{(datetime.now().date().month + 3) if (datetime.now().date().month+3)<=12 else (datetime.now().date().month+3-12)}-{datetime.now().date().day}"
    if request.method == 'POST':
        origin = request.POST.get('Origin')
        destination = request.POST.get('Destination')
        depart_date = request.POST.get('DepartDate')
        #seat = request.POST.get('SeatClass')
        trip_type = request.POST.get('TripType')
        if(trip_type == '1'):
            return render(request, 'admin/local.html', locals(),{
            'origin': origin,
            'destination': destination,
            'depart_date': depart_date,
            #'seat': seat.lower(),
            'trip_type': trip_type
        })
        elif(trip_type == '2'):
            return_date = request.POST.get('ReturnDate')
            return render(request, 'admin/local.html', locals(),{
            'min_date': min_date,
            'max_date': max_date,
            'origin': origin,
            'destination': destination,
            'depart_date': depart_date,
            #'seat': seat.lower(),
            'trip_type': trip_type,
            'return_date': return_date
        })
    else:
        return render(request, 'admin/local.html',locals(), {
            'min_date': min_date,
            'max_date': max_date
        })
        
def query(request, q):
    places = Place.objects.all()
    filters = []
    q = q.lower()
    for place in places:
        if (q in place.city.lower()) or (q in place.airport.lower()) or (q in place.code.lower()) or (q in place.country.lower()):
            filters.append(place)
    return JsonResponse([{'code':place.code, 'city':place.city, 'country': place.country} for place in filters], safe=False)

def flight(request):
    o_place = request.GET.get('Origin')
    d_place = request.GET.get('Destination')
    trip_type = request.GET.get('TripType')
    departdate = request.GET.get('DepartDate')
    depart_date = datetime.strptime(departdate, "%Y-%m-%d")
    return_date = None
    if trip_type == '2':
        returndate = request.GET.get('ReturnDate')
        return_date = datetime.strptime(returndate, "%Y-%m-%d")
        #flightday2 = Flight.objects.get(depart_day=returndate) ##
        origin2 = Place.objects.get(code=d_place)   ##.upper()
        destination2 = Place.objects.get(code=o_place)  ##.upper()
    #seat = request.GET.get('SeatClass')
    #flightday =Flight.objects.get(depart_day=departdate)
    #flightday = Week.objects.get(number=depart_date.weekday())
    destination = Place.objects.get(code=d_place)    ##.upper()
    origin = Place.objects.get(code=o_place)     ##.upper()
    #if seat == 'economy':
    flights = Flight.objects.filter(depart_day=departdate,origin=origin,destination=destination).exclude(fare=0).order_by('fare')#.exclude(economy_fare=0).order_by('economy_fare')
    """try:
            max_price = flights.last().fare#.economy_fare
            min_price = flights.first().fare#.economy_fare
    except:
            max_price = 0
            min_price = 0
"""
    if trip_type == '2':    ##
          flights2 = Flight.objects.filter(depart_day=returndate,origin=origin2,destination=destination2).exclude(fare=0).order_by('fare')#.exclude(economy_fare=0).order_by('economy_fare')    ##
    """try:
                max_price2 = flights2.last().fare#.economy_fare   ##
                min_price2 = flights2.first().fare#.economy_fare  ##
            except:
                max_price2 = 0  ##
                min_price2 = 0  ##
                
    elif seat == 'business':
        flights = Flight.objects.filter(depart_day=flightday,origin=origin,destination=destination).exclude(business_fare=0).order_by('business_fare')
        try:
            max_price = flights.last().business_fare
            min_price = flights.first().business_fare
        except:
            max_price = 0
            min_price = 0

        if trip_type == '2':    ##
            flights2 = Flight.objects.filter(depart_day=flightday2,origin=origin2,destination=destination2).exclude(business_fare=0).order_by('business_fare')    ##
            try:
                max_price2 = flights2.last().business_fare   ##
                min_price2 = flights2.first().business_fare  ##
            except:
                max_price2 = 0  ##
                min_price2 = 0  ##

    elif seat == 'first':
        flights = Flight.objects.filter(depart_day=flightday,origin=origin,destination=destination).exclude(first_fare=0).order_by('first_fare')
        try:
            max_price = flights.last().first_fare
            min_price = flights.first().first_fare
        except:
            max_price = 0
            min_price = 0
            
        if trip_type == '2':    ##
            flights2 = Flight.objects.filter(depart_day=flightday2,origin=origin2,destination=destination2).exclude(first_fare=0).order_by('first_fare')
            try:
                max_price2 = flights2.last().first_fare   ##
                min_price2 = flights2.first().first_fare  ##
            except:
                max_price2 = 0  ##
                min_price2 = 0  ##    ##
"""
    #print(calendar.day_name[depart_date.weekday()])
    if trip_type == '2':
        return render(request, "admin/flight.html", {
            'flights': flights,
            'origin': origin,
            'destination': destination,
            'flights2': flights2,   ##
            'origin2': origin2,    ##
            'destination2': destination2,    ##
            #'seat': seat.capitalize(),
            'trip_type': trip_type,
            'depart_date': depart_date,
            'return_date': return_date,
            #'max_price': math.ceil(max_price/100)*100,
            #'min_price': math.floor(min_price/100)*100,
            #'max_price2': math.ceil(max_price2/100)*100,    ##
            #'min_price2': math.floor(min_price2/100)*100    ##
        })
    else:
        return render(request, "admin/flight.html", {
            'flights': flights,
            'origin': origin,
            'destination': destination,
            #'seat': seat.capitalize(),
            'trip_type': trip_type,
            'depart_date': depart_date,
            'return_date': return_date,
            #'max_price': math.ceil(max_price/100)*100,
            #'min_price': math.floor(min_price/100)*100
        })
def review(request):
    flight_1 = request.GET.get('flight1Id')
    date1 = request.GET.get('flight1Date')
    #seat = request.GET.get('seatClass')
    round_trip = False
    if request.GET.get('flight2Id'):
        round_trip = True

    if round_trip:
        flight_2 = request.GET.get('flight2Id')
        date2 = request.GET.get('flight2Date')

    if request.user.is_authenticated:
        flight1 = Flight.objects.get(id=flight_1)
        flight1ddate = datetime(int(date1.split('-')[2]),int(date1.split('-')[1]),int(date1.split('-')[0]),flight1.depart_time.hour,flight1.depart_time.minute)
        flight1adate = flight1ddate
        flight2 = None
        flight2ddate = None
        flight2adate = None
        if round_trip:
            flight2 = Flight.objects.get(id=flight_2)
            flight2ddate = datetime(int(date2.split('-')[2]),int(date2.split('-')[1]),int(date2.split('-')[0]),flight2.depart_time.hour,flight2.depart_time.minute)
            flight2adate = flight2ddate
        #print("//////////////////////////////////")
        #print(f"flight1ddate: {flight1adate-flight1ddate}")
        #print("//////////////////////////////////")
        if round_trip:
            return render(request, "admin/book.html", {
                'flight1': flight1,
                'flight2': flight2,
                "flight1ddate": flight1ddate,
                "flight1adate": flight1adate,
                "flight2ddate": flight2ddate,
                "flight2adate": flight2adate,
                #"seat": seat,
                #"fee": FEE
            })
        return render(request, "admin/book.html", {
            'flight1': flight1,
            "flight1ddate": flight1ddate,
            "flight1adate": flight1adate,
            #"seat": seat,
            #"fee": FEE
        })
    else:
        return HttpResponseRedirect(reverse("login"))

def book(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            flight_1 = request.POST.get('flight1')
            flight_1date = request.POST.get('flight1Date')
            #flight_1class = request.POST.get('flight1Class')
            f2 = False
            if request.POST.get('flight2'):
                flight_2 = request.POST.get('flight2')
                flight_2date = request.POST.get('flight2Date')
                #flight_2class = request.POST.get('flight2Class')
                f2 = True
            countrycode = request.POST['countryCode']
            mobile = request.POST['mobile']
            #email = request.POST['email']
            flight1 = Flight.objects.get(id=flight_1)
            if f2:
                flight2 = Flight.objects.get(id=flight_2)
            fname = request.POST['fname']
            lname = request.POST['lname']
            gender = request.POST['gender']
            pas=Passenger.objects.create(first_name=fname,last_name=lname,gender=gender.lower())
            pas.save()
            #coupon = request.POST.get('coupon')
            
            try:
                ticket1 = createticket(request.user,pas,flight1,flight_1date,countrycode,mobile)
                fare = flight1.fare
                ticket1.status = 'CONFIRMED'
                ticket1.booking_date = datetime.now()
                ticket1.save()
                flight1 = Flight.objects.get(id=flight_1)
                flight1.number_booking=flight1.number_booking+1
                flight1.save()
                send_mail('Booking Confirmation','Your bookinng process has been succeeded',
                      settings.EMAIL_HOST_USER,[request.user.email],fail_silently=False)
                
                if f2:
                    ticket2 = createticket(request.user,pas,flight2,flight_2date,countrycode,mobile)
                    fare = (flight1.fare)+(flight2.fare)
                    ticket2.status = 'CONFIRMED'
                    ticket2.save()
                    flight2 = Flight.objects.get(id=flight_2)
                    flight2.number_booking=flight1.number_booking+1
                    flight2.save()
                # if(flight_1class == 'Economy'):
                    # if f2:
                        # fare = (flight1.fare*int(passengerscount))+(flight2.fare*int(passengerscount))
                    # else:
                        # fare = flight1.fare*int(passengerscount)
                # elif (flight_1class == 'Business'):
                    # if f2:
                        # fare = (flight1.business_fare*int(passengerscount))+(flight2.business_fare*int(passengerscount))
                    # else:
                        # fare = flight1.business_fare*int(passengerscount)
                # elif (flight_1class == 'First'):
                    # if f2:
                        # fare = (flight1.first_fare*int(passengerscount))+(flight2.first_fare*int(passengerscount))
                    # else:
                        # fare = flight1.first_fare*int(passengerscount)
            except Exception as e:
                return HttpResponse(e)            
            if f2:    ##
                return render(request, "admin/payprocess.html", { ##
                    'fare': fare,   ##
                    'ticket': ticket1.id,   ##
                    'ticket2': ticket2.id,   ##
                    'ticket2email': ticket2.email
                })  ##
            return render(request, "admin/payprocess.html",{'ticket': ticket1.id,'fare': fare,})
        else:
            return HttpResponseRedirect(reverse("login"))
    else:
        return HttpResponse("Method must be post.")
       
"""def payment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ticket_id = request.POST['ticket']
            ticket_email = request.POST['ticketemail']           
            t2 = False
            if request.POST.get('ticket2'):
                ticket2_id = request.POST['ticket2']
                ticket_email2 = request.POST['ticket2email']
                t2 = True
            fare = request.POST.get('fare')
            card_number = request.POST['cardNumber']
            card_holder_name = request.POST['cardHolderName']
            exp_month = request.POST['expMonth']
            exp_year = request.POST['expYear']
            cvv = request.POST['cvv']
            try:
                ticket = Ticket.objects.get(id=ticket_id)
                ticket.status = 'CONFIRMED'
                ticket.booking_date = datetime.now()
                ticket.save()
                send_mail('Booking Confirmation','Your bookinng process has been succeeded',
                      settings.EMAIL_HOST_USER,[request.user.email],fail_silently=False)
                 
                if t2:
                    ticket2 = Ticket.objects.get(id=ticket2_id)
                    ticket2.status = 'CONFIRMED'
                    ticket2.save()
                    return render(request, 'admin/payment_process.html', {
                        'ticket1': ticket,
                        'ticket2': ticket2
                    })
                return render(request, 'admin/payment_process.html', {
                    'ticket1': ticket,
                    'ticket2': ""
                })
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Method must be post.")
    else:
        return HttpResponseRedirect(reverse('login'))     
def resume_booking(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            ref = request.POST['ref']
            ticket = Ticket.objects.get(ref_no=ref)
            if ticket.user == request.user:
                return render(request, "admin/payment.html", {
                    'fare': ticket.total_fare,
                    'ticket': ticket.id
                })
            else:
                return HttpResponse("User unauthorised")
        else:
            return HttpResponseRedirect(reverse("login"))
    else:
        return HttpResponse("Method must be post.")"""
def sectiongallery(request):
    photos=Gallery.objects.all()
    return render(request, 'admin/sectiongallery.html',{'photos':photos })
def visasection(request):
  if request.method == "POST":
    if request.user.is_authenticated:
        name1 = request.POST['name']
        contact1 = request.POST['contact']
        typev1 = request.POST["typev"]
        try:
           visa1=createvisa(request.user,name1,contact1,typev1)
        except Exception as e:
                return HttpResponse(e)
        return render(request, "admin/visasection.html", { "message": " Your forum is successfully filled ✓ ",
        'visa1': visa1.id_visa})
    else:
            return HttpResponseRedirect(reverse("login"))
  else:
        return render(request, 'admin/visasection.html')       
  #return render(request, 'admin/visasection.html')
def cvresume(request):
  if request.method == "POST":
    if request.user.is_authenticated:
        n1= request.POST['name']
        ad1= request.POST['adress']
        tel1= request.POST['tel']
        e1= request.POST['email'] 
        c1= request.POST['career'] 
        y1= request.POST['year']
        co1= request.POST['course']
        ex1= request.POST['exp']
        a1 = request.POST['act']
        s1= request.POST['skill']
        w1= request.POST['wit']
        try:
           cv1 = CVResume.objects.create()
           cv1.user = request.user
           cv1.name= n1
           cv1.address= ad1
           cv1.Telephone= tel1
           cv1.Email= e1
           cv1.Career_objective= c1
           cv1.Year_admission_university= y1
           cv1.courses= co1
           cv1.experiences= ex1
           cv1.activities= a1
           cv1.skills= s1
           cv1.witnesses= w1
           cv1.save()           
        except Exception as e:
                return HttpResponse(e)
        return render(request, "admin/cvresume.html",{"message": " Your CV has been uploaded ✓ ",})
    else:
            return HttpResponseRedirect(reverse("login"))
  else:
        return render(request, 'admin/cvresume.html')
    #return render(request, 'admin/cvresume.html')
def Destinations(request):
  if request.method == "POST":
    if request.user.is_authenticated:
        name1 = request.POST['name']
        contact1 = request.POST['contact']
        email1 = request.POST["email"]  
        types1 = request.POST["types"]   
        how1 = request.POST["how"]        
        try:
           st = studyserv.objects.create()
           st.user = request.user
           st.Name= name1
           st.Contact=contact1
           st.Email=email1
           st.ServiceType=types1
           st.How=how1
           st.save()           
        except Exception as e:
                return HttpResponse(e)
        return render(request, "admin/Destinations.html", { "message": " Your forum is successfully filled ✓ ",})
    else:
            return HttpResponseRedirect(reverse("login"))
  else:
        return render(request, 'admin/Destinations.html')
    #return render(request, 'admin/Destinations.html')
def Services(request):
  if request.method == "POST":       
        return render(request, "admin/Destinations.html")
  else:
        return render(request, 'admin/Services.html')
def courses(request):
    C=Courses.objects.all() 
    #courseI = request.GET['courseId']
    #courseI = request.POST.get('courseId')        
    if request.method == "POST":       
        courseI= request.POST.get('courseId')
        course1 = Courses.objects.get(id=courseI)
        return render(request, "admin/Courses.html", locals(),{'course1':course1,
        'courseId':courseI})
    else:
        return render(request,  'admin/Courses.html', locals())
    #return render(request, 'admin/Courses.html', locals())
def coursereg(request):
  courseIDD = request.GET.get('courseId')
  #coursetopic = request.GET.get('topic')
   
  if request.method == "POST":
    if request.user.is_authenticated:
        coursee = request.POST['courseI']
        cc = Courses.objects.get(id=coursee)
        name1 = request.POST['name']
        contact1 = request.POST['contact']
        email1 = request.POST["email"]        
        try:
           cs=createcoursespart(request.user,cc,name1,contact1,email1)         
        except Exception as e:
                return HttpResponse(e)
        #return HttpResponse("you are registred in the course.")
        return render(request, "admin/coursereg.html", { "message": " Your forum is successfully filled ✓ you can not register again !",})
    else:
            return HttpResponseRedirect(reverse("login"))
  else:
        course1 = Courses.objects.get(id=courseIDD)
        return render(request, 'admin/coursereg.html',{'courseI':courseIDD,
        'course1':course1})