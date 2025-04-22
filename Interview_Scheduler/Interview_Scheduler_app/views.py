from django.shortcuts import render
from .models import Assignment,Applicant,InterviewSlot

# Create your views here.
def dashboard(request):

    return render(request,"dashboard.html")

def applicants(request):
    applicants=Applicant.objects.all()
    return render(request,'applicants.html',{"applicants":applicants})

def slots(request):
    interviews_slots=InterviewSlot.objects.all()
    return render(request,'slots.html',{"interviews_slots":interviews_slots})

def assignments(request):
    assignments=Assignment.objects.select_related('interview_slot','applicant')
    return render(request,'assignments.html',{"assignments":assignments})

def add_applicant(request):
    return render(request,'add_applicant.html')

def add_slot(request):
    return render(request,'add_slot.html')

def add_assignment(request):
    return render(request,'add_assignment.html')