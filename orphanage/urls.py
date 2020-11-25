from django.urls import path

from . import views
urlpatterns=[
    path('parentform/',views.parentform,name='parentform'),
    path('sample_view/', views.sample_view, name='sample_view'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('adoption_form/', views.adoption_form, name='adoption_form')
]