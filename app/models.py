from django.db import models
from datetime import date

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    player_id = models.CharField(max_length=20,blank=True)
    player_name = models.CharField(max_length=200,blank=True)
    innings = models.CharField(max_length=10,blank=True)
    top_score = models.CharField(max_length=10,blank=True)
    average = models.CharField(max_length=10,blank=True)
    strike_rate = models.CharField(max_length=10,blank=True)
    sixes = models.CharField(max_length=10,blank=True)
    fours = models.CharField(max_length=10,blank=True)
    overs = models.CharField(max_length=10,blank=True)
    economy = models.CharField(max_length=10,blank=True)
    team_id = models.CharField(max_length=100,default='7680305',blank=True)
    total_matches = models.CharField(max_length=30,blank=True)
    total_wickets = models.CharField(max_length=30,blank=True)
    total_runs = models.CharField(max_length=30,blank=True)
    team_name = models.CharField(max_length=300,default='Lucky Cricket Aca',blank=True)
    birthdate = models.DateField()
    gender = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=200)
    mobile = models.IntegerField()
    game_type = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="photos/", null=True, blank=True)
    document = models.FileField(upload_to="docs/", null=True, blank=True)

    @property
    def age(self):
        from datetime import date
        today = date.today()

        return today.year - self.birthdate.year - (
            (today.month, today.day) < (self.birthdate.month, self.birthdate.day)
        )

    @property
    def paid(self):
        from .models import FeePayment   # import inside to avoid circular import
        
        today = date.today()
        return FeePayment.objects.filter(
            student=self,
            month=today.month,
            year=today.year
        ).exists()
    
    def __str__(self):
        return self.name
    
class FeePayment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="payments")
    month = models.IntegerField()
    year = models.IntegerField()
    amount = models.FloatField(blank=True)
    paid_on = models.DateField(default=date.today)
    remarks = models.CharField(max_length=200, blank=True)

    class Meta:
        unique_together = ('student', 'month', 'year')  # Avoid duplicate payments

    def __str__(self):
        return f"{self.student.name} - {self.month}/{self.year}"