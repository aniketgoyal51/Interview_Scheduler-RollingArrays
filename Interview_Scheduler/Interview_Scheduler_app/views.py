from django.shortcuts import render,redirect
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
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        job_applied_for = request.POST.get("job_applied_for")
        Applicant.objects.create(name=name, email=email, job_applied_for=job_applied_for)
        return redirect('applicants')  # Or another view, like applicant list

    return render(request, 'add_applicant.html')

def add_slot(request):
    if request.method == "POST":
        date = request.POST.get("date")
        time = request.POST.get("time")
        interviewer = request.POST.get("interviewer_name")
        job_role = request.POST.get("job_role")
        InterviewSlot.objects.create(date=date, time=time, interviewer_name=interviewer, job_role=job_role)
        return redirect('slots')

    return render(request, 'add_slot.html')

def add_assignment(request):
    if request.method == "POST":
        applicant_id = request.POST.get("applicant")
        slot_id = request.POST.get("interview_slot")

        applicant = Applicant.objects.get(id=applicant_id)
        slot = InterviewSlot.objects.get(id=slot_id)

        Assignment.objects.create(applicant=applicant, interview_slot=slot)

        slot.status = "scheduled"
        slot.save()

        return redirect('assignments')

    applicants = Applicant.objects.all()
    slots = InterviewSlot.objects.filter(status="available")

    return render(request, 'add_assignment.html', {
        "applicants": applicants,
        "slots": slots,
    })