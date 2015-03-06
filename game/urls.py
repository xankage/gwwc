from django.conf.urls import patterns, url
from game import views

urlpatterns = patterns ('',
  url(r'^$', views.index, name='index'),
  url(r'^charity/(?P<charity_name_slug>[\w\-]+)/$', views.charity, name='charity'),
  url(r'^charity/', views.charities, name='charities'),
  url(r'^about/', views.about, name='about'),
  url(r'^contact/', views.contact, name='contact'),
)
