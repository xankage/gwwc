from django.shortcuts import render
from game.models import Charity, Event, Person, Site 

def index(request):
  context_dict = {}
  leading_charity = Charity.objects.order_by('score')[0]
  context_dict['leading_charity'] = leading_charity
  return render(request, 'game/index.html', context_dict)

def charities(request):
  context_dict = {}
  charities = Charity.objects.order_by('score')
  context_dict['charsities'] = charities
  return render(request, 'game/charities.html', context_dict)

def charity(request, charity_name_slug):
  context_dict = {}
  try:
    charity = Charity.objects.get(slug = charity_name_slug)
    events = Event.objects.filter(charity = charity)
    context_dict['charity'] = charity
    context_dict['events'] = events
  except Charity.DoesNotExist:
    pass
  return render(request, 'game/charity.html', context_dict)

def about(request):
  context_dict = {}
  return render(request, 'game/about.html', context_dict)

def contact(request):
  context_dict = {}
  people = Person.objects.all()
  sites = Site.objects.all()
  context_dict['people'] = people
  context_dict['sites'] = sites
  return render(request, 'game/contact.html', context_dict)
