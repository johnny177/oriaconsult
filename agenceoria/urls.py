from django.urls import path
from . import views


from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.index, name="index"),
    path("eventpar", views.eventpar, name="eventpar"),
    path("login", views.login_view, name="login"),
    path("query/places/<str:q>", views.query, name="query"),
    path("local", views.local, name="local"),
    path("local/flight", views.flight, name="flight"),
    path("local/flight/book", views.book, name="book"),
    path("review", views.review, name="review"),    
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),    
    #path("payment", views.payment, name="payment"),
    #path('resume', views.resume_booking, name="resumebooking"),  
    path("international", views.international, name="international"), 
    path("sectiongallery", views.sectiongallery, name="sectiongallery"),
    path("visasection", views.visasection, name="visasection"),
    path("cvresume", views.cvresume, name="cvresume"),
    path("Services/Destinations", views.Destinations, name="Destinations"),
    path("Services", views.Services, name="Services"),
    path("Courses", views.courses, name="Courses"),
    path("Courses/register", views.coursereg, name="courseregister"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
