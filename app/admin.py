from django.contrib import admin
from . models import Student,FeePayment

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','birthdate','mobile','game_type']


class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ['student','paid_on']

admin.site.register(Student)
admin.site.register(FeePayment)