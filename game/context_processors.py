from game.models import Charity

def global_charities(request):
  charities = Charity.objects.order_by('score')
  return {'charities': charities}
