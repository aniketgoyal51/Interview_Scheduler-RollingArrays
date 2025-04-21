from django.db import models

# Create your models here.
class Applicant(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    job_applied_for=models.CharField(max_length=100)


class InterviewSlot(models.Model):
    status_choices = [
        ("available","Available"), 
        ("scheduled","Scheduled"), 
        ("completed","Completed"), 
        ("cancelled","Cancelled")
    ]

    date=models.DateField()
    time=models.TimeField()
    interviewer_name=models.CharField(max_length=100)
    job_role=models.CharField(max_length=100)
    status=models.CharField(max_length=20,choices=status_choices,default="available")

class Assignment(models.Model):
    interview_slot=models.ForeignKey(InterviewSlot, on_delete=models.CASCADE)
    applicant=models.ForeignKey(Applicant, on_delete=models.CASCADE)
