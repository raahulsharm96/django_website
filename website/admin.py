from django.contrib import admin
from website.models import Member
from .models import Resume
# Register your models here.

admin.site.register(Member)

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ["fname", "lname","email","age","skills","CTC","Experience","resume"]       