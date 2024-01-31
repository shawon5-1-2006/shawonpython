from django.contrib import admin
from About_us.models import Teachers

# Register your models here.
class TeachersAdmin(admin.ModelAdmin):
    list_display=('T_Name', 'T_Email')
admin.site.register(Teachers, TeachersAdmin)
