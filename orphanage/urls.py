from django.urls import path

from . import views
urlpatterns=[
    path('parentform/',views.parentform,name='parentform'),
    path('', views.sample_view, name='sample_view'),
    path('submit_parent/', views.submit_parent, name='submit_parent'),
    path('adoptionform/', views.adoptionform, name='adoptionform'),
    path('donationform/', views.donationform, name='donationform'),
    path('submit_adoption/', views.submit_adoption, name='submit_adoption'),
    path('submit_donation/', views.submit_donation, name='submit_donation'),
    path('view_parent/',views.view_parent,name="view_parent"),
    path('submit_orphan/', views.submit_orphan, name='submit_orphan'),
    path('submit_donor/', views.submit_donor, name='submit_donor'),
    path('donorform/', views.donorform, name='donorform'),
    path('orphanform/',views.orphanform,name='orphanform'),
]