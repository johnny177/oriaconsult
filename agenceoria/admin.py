from django.contrib import admin

# Register your models here.
from .models import *

class MembershipInline_Coursespart(admin.TabularInline):
    model = Coursespart
    extra = 0    
    list_display = ()
    verbose_name = "participant"
    verbose_name_plural = "participants"
    def get_readonly_fields(self, request, obj=None):        
            return ['user','course','Name','Contact','Email']      
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
class MembershipInline_Eventpart(admin.TabularInline):
    model = Eventspart
    extra = 0    
    list_display = ()
    verbose_name = "participant"
    verbose_name_plural = "participants"
    def get_readonly_fields(self, request, obj=None):
        
            return ['user','Event','Name','Contact','Email']
       
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
# class MembershipInlinePassenger(admin.TabularInline):
    # model = Passenger
    # extra = 0
    # show_change_link=True
    # fields = ('first_name','last_name','gender')
class AdminGallery(admin.ModelAdmin):
   list_display = ('tag','Picture')
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': ['tag','Picture']}),                     
              ] 
# class AdminFeedback(admin.ModelAdmin):
   # list_display = ('comment','Picture')
   # fieldsets = [    
       # ('Details', {
            # 'classes': ('',),
            # 'fields': ['comment','Picture']}),                     
              # ]
              
class AdminPlace(admin.ModelAdmin):
   list_display = ('city','airport','code','country','typep')
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': ['city','airport','code','country','typep']}),                     
              ]
class AdminFlight(admin.ModelAdmin):
   list_display = ('origin','destination','depart_day','depart_time','arrival_time','fare','max_booking','number_booking')
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': ['origin','destination','depart_day','depart_time','arrival_time','fare','max_booking','number_booking']}),                     
              ] 
"""class AdminPassenger(admin.ModelAdmin):
   list_display = ('first_name','last_name','gender')
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': ['first_name','last_name','gender']}),                     
              ] """
class AdminTicket(admin.ModelAdmin):
   list_display = ('user','ref_no','passengers','flight','flight_ddate','flight_adate','flight_fare','total_fare','booking_date','mobile','email','status')
   #inlines = (MembershipInlinePassenger,)
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': ['user','ref_no','passengers','flight','flight_ddate','flight_adate','flight_fare','total_fare','booking_date','mobile','email','status']}),                     
              ] 
   def get_readonly_fields(self, request, obj=None):
        
            return ['user','ref_no','passengers','flight','flight_ddate','flight_adate','flight_fare','total_fare','booking_date','mobile','email','status']
"""class AdminStudyAbroad(admin.ModelAdmin):
   list_display = ()
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': []}),                     
              ] 
class AdminIELTS(admin.ModelAdmin):
   list_display = ()
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': []}),                     
              ] 
class AdminScholarship(admin.ModelAdmin):
   list_display = ()
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': []}),                     
              ] 
class AdminHotelBooking(admin.ModelAdmin):
   list_display = ()
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': []}),                     
              ] 
class AdminCVResume(admin.ModelAdmin):
   list_display = ('cv',)
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': ['cv']}),                     
              ] 
class AdminStudentProfile(admin.ModelAdmin):
   list_display = ()
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': []}),                     
              ] 

class AdminInterviewTraining(admin.ModelAdmin):
   list_display = ()
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': []}),                     
              ] 
class AdminHotel(admin.ModelAdmin):
   list_display = ('name','region')
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': ['name','region']}),                     
              ] 
class AdminUniversities(admin.ModelAdmin):
   list_display = ('name','country')
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': ['name','country']}),                     
              ]
"""
class Adminvisa(admin.ModelAdmin):
   list_display = ('user','Name','Contact','Type')
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': ['user','Name','Contact','Type']}),                     
              ]  
class AdminCVResume(admin.ModelAdmin):
   list_display = ('user','name','address','Telephone','Email','Career_objective','Year_admission_university','courses','experiences','activities','skills','witnesses')
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': ['user','name','address','Telephone','Email','Career_objective','Year_admission_university','courses','experiences','activities','skills','witnesses']}),                     
              ]  
class Adminstudyserv(admin.ModelAdmin):
   list_display = ('user','Name','Contact','Email','ServiceType','How')
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': ['user','Name','Contact','Email','ServiceType','How']}),                     
              ] 
class AdminCourses(admin.ModelAdmin):
   list_display = ('topic','description','country','city','date','datetime','duration')
   #inlines = (MembershipInlinePassenger,)
   inlines = (MembershipInline_Coursespart,)
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': ['topic','description',('country','city'),('date','datetime','duration')]}),                     
              ]              
class AdminCoursespart(admin.ModelAdmin):
   list_display = ('user','course','Name','Contact','Email')
   
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': ['user','course','Name','Contact','Email']}),                     
              ]
class AdminEvents(admin.ModelAdmin):
   list_display = ('topic','description','country','city','date','datetime')
   #inlines = (MembershipInlinePassenger,)
   inlines = (MembershipInline_Eventpart,)
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': ['topic','description',('country','city'),('date','datetime')]}),                     
              ]              
class AdminEventspart(admin.ModelAdmin):
   list_display = ('user','Event','Name','Contact','Email')   
   fieldsets = [    
       ('Details', {
            'classes': ('',),
            'fields': ['user','Event','Name','Contact','Email']}),                     
              ]
admin.site.register(Gallery,AdminGallery)
admin.site.register(studyserv,Adminstudyserv)
admin.site.register(Place,AdminPlace)
admin.site.register(Flight,AdminFlight)
#admin.site.register(Passenger,AdminPassenger)
admin.site.register(Ticket,AdminTicket)
admin.site.register(visa,Adminvisa)
admin.site.register(Courses,AdminCourses)
admin.site.register(Coursespart,AdminCoursespart)
admin.site.register(Events,AdminEvents)
admin.site.register(Eventspart,AdminEventspart)
admin.site.register(CVResume,AdminCVResume)
#admin.site.register(StudentProfile,AdminStudentProfile)
#admin.site.register(InterviewTraining,AdminInterviewTraining)
#admin.site.register(Hotel,AdminHotel)
#admin.site.register(Universities,AdminUniversities)