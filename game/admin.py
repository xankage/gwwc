from django.contrib import admin
from game.models import Charity, Person, Site 

class CharityAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Charity)
admin.site.register(Person)
admin.site.register(Site)
