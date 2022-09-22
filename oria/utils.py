from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from agenceoria.models import *
import secrets
from datetime import datetime, timedelta
from xhtml2pdf import pisa

from agenceoria.constant import FEE

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def createticket(user,passenger,flight1,flight_1date,countrycode,mobile):
    ticket = Ticket.objects.create()
    ticket.user = user
    ticket.ref_no = secrets.token_hex(3).upper()
    ticket.passengers=passenger
    ticket.flight = flight1
    ticket.flight_ddate = datetime(int(flight_1date.split('-')[2]),int(flight_1date.split('-')[1]),int(flight_1date.split('-')[0]))
    ###################
    flight1ddate = datetime(int(flight_1date.split('-')[2]),int(flight_1date.split('-')[1]),int(flight_1date.split('-')[0]),flight1.depart_time.hour,flight1.depart_time.minute)
    flight1adate = flight1ddate
    ###################
    ticket.flight_adate = datetime(flight1adate.year,flight1adate.month,flight1adate.day)
    ffre = 0.0
    # if flight_1class.lower() == 'first':
    ticket.flight_fare = flight1.fare
    ffre = flight1.fare
    # elif flight_1class.lower() == 'business':
        # ticket.flight_fare = flight1.business_fare*int(passengerscount)
        # ffre = flight1.business_fare*int(passengerscount)
    # else:
        # ticket.flight_fare = flight1.economy_fare*int(passengerscount)
        # ffre = flight1.economy_fare*int(passengerscount)
    #ticket.other_charges = FEE
    # if coupon:
        # ticket.coupon_used = coupon                     ##########Coupon
    ticket.total_fare = ffre  #+FEE+0.0                    ##########Total(Including coupon)
    # ticket.seat_class = flight_1class.lower()
    ticket.status = 'PENDING'
    ticket.mobile = ('+'+countrycode+' '+mobile)
    #ticket.email = email
    ticket.save()
    return ticket
def createvisa(user,name,contact,typev):
    visa1 = visa.objects.create()
    visa1.user = user
    visa1.Name=name
    visa1.Contact=contact
    visa1.Type=typev
    visa1.save()
    return visa1
def createcoursespart(user,coursee,name,contact,email):
    cp = Coursespart.objects.create()
    cp.user = user
    cp.course=coursee
    cp.Name= name
    cp.Contact=contact
    cp.Email=email
    cp.save()
    return cp