from django.contrib import admin
from .models import Student, Staff, Complaint, Hostel
# Register your models here.

admin.site.register(Student)
admin.site.register(Complaint)
admin.site.register(Hostel)
admin.site.register(Staff)