from django.contrib import admin

from .models import Session, Cabin, Course, Counselor, Camper, Registration, Period, Year

admin.site.register(Period)
admin.site.register(Year)
admin.site.register(Session)
admin.site.register(Cabin)
admin.site.register(Course)
admin.site.register(Counselor)
admin.site.register(Camper)
admin.site.register(Registration)
