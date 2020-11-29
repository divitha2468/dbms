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
]