from django.urls import path


from . import views
app_name="orphanage"
urlpatterns=[
    path('parentform/',views.parentform,name='parentform'),
    path('sample_view', views.sample_view, name='sample_view'),
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
    path('view_orphan/', views.view_orphan, name="view_orphan"),
    path('view_donor/', views.view_donor, name="view_donor"),
    path('view_donationhistory/', views.view_donationhistory, name="view_donationhistory"),
    path('view_adoptionhistory/', views.view_adoptionhistory, name="view_adoptionhistory"),
    path('submit_adopt/', views.submit_adopt, name="submit_adopt"),
    path('submit_age/', views.submit_age, name="submit_age"),
    path('submit_cash/', views.submit_cash, name="submit_cash"),
    path('submit_year/', views.submit_year, name="submit_year"),
    path('submit_year2/', views.submit_year2, name="submit_year2"),
    #path('', views.login, name="login"),
    # path('deletestaff/', views.deletestaff, name="deletestaff"),
    # path('submit_delete/', views.submit_delete, name="submit_delete"),
    path('',views.login,name="login"),
    # path("register/",views.register,name="register"),
    path("logout/",views.logout_request,name="logout")
]