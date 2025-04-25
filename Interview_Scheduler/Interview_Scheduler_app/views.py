from django.shortcuts import render,redirect,get_object_or_404
from .models import Assignment,Applicant,InterviewSlot

# Create your views here.
def dashboard(request):
    total_applicants = Applicant.objects.count()
    total_slots = InterviewSlot.objects.count()
    scheduled_interviews = InterviewSlot.objects.filter(status='scheduled').count()
    completed_interviews = InterviewSlot.objects.filter(status='completed').count()
    available_interviews = InterviewSlot.objects.filter(status='available').count()

    recent_assignments = Assignment.objects.select_related('applicant', 'interview_slot').order_by('-id')[:5]

    assignment_data = []
    for assignment in recent_assignments:
        slot = assignment.interview_slot
        if slot.status == 'completed':
            status_class = 'bg-green-200 text-green-800'
        elif slot.status == 'scheduled':
            status_class = 'bg-yellow-200 text-yellow-800'
        else:
            status_class = 'bg-blue-200 text-blue-800'
        
        assignment_data.append({
            'applicant_name': assignment.applicant.name,
            'interviewer_name': assignment.interview_slot.interviewer_name,
            'slot': f"{slot.date}, {slot.time}",
            'status': slot.status.capitalize(),
            'status_class': status_class,
        })
    context = {
        'total_applicants': total_applicants,
        'total_slots': total_slots,
        'scheduled_interviews': scheduled_interviews,
        'completed_interviews': completed_interviews,
        'recent_assignments': assignment_data,
        'available_interviews':available_interviews
    }
    print(context)
    return render(request, 'dashboard.html', context)

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


def update_slot(request,slot_id):
    slot=InterviewSlot.objects.get(id=slot_id)
    if slot.status=='scheduled':
        slot.status="completed"
        slot.save()
    return redirect("assignments")

def cancel_slot(request, slot_id):
    if request.method == 'POST':
        slot = get_object_or_404(InterviewSlot, id=slot_id)
        slot.status = 'cancelled'
        slot.save()
    return redirect('slots') 

def filter_date(request):
    date = request.GET.get('date')
    if date:
        assignments = Assignment.objects.filter(interview_slot__date=date)
    else:
        assignments = Assignment.objects.all()
    return render(request, 'assignments.html', {'assignments': assignments})


def filtur_status(request):
    filter_status = request.GET.get('status')
    if filter_status:
        slots = InterviewSlot.objects.filter(status=filter_status)
    else:
        slots = InterviewSlot.objects.all()
    return render(request, 'slots.html', {'interviews_slots': slots})