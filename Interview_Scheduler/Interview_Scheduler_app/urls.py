from django.urls import path
from . import views

urlpatterns=[
    path('',views.dashboard,name='dashboard'),
    path('applicants',views.applicants,name='applicants'),
    path('add_applicant',views.add_applicant,name='add_applicant'),
    path('slots',views.slots,name='slots'),
    path('add_slot',views.add_slot,name='add_slot'),
    path('assignments',views.assignments,name='assignments'),
    path('add_assignment',views.add_assignment,name='add_assignment'),
    path('update_slot/<int:slot_id>/',views.update_slot,name='update_slot'),
    path('cancel_slot/<int:slot_id>/', views.cancel_slot, name='cancel_slot'),
    path('assignments/', views.filter_date, name='filter_date'),
    path('slots/', views.filtur_status, name='filtur_status')
]