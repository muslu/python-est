urlpatterns = patterns('',

    url(r'^$', views.AnaSayfa),
    
    
    url(r'^odeme/$', views.Odeme),
    url(r'^payodeme/$', views.PayOdeme),
    

    url(r'^admin/', include(admin.site.urls)),
)
