from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Charity(models.Model):
  title = models.CharField(max_length = 128, unique = True)
  description = models.CharField(max_length = 1024)
  money_raised = models.IntegerField(default = 0)
  people_reached = models.IntegerField(default = 0)
  money_used = models.IntegerField(default = 0)
  people_used = models.IntegerField(default = 0)
  time_used = models.IntegerField(default = 0)
  link = models.URLField(max_length = 128)
  score = models.IntegerField(default = 0)
  slug = models.SlugField(unique = True, blank = True)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Charity, self).save(*args, **kwargs)

  def __unicode__(self):
    return self.title

  class Meta:
    verbose_name_plural = "charities"

class Person(models.Model):
  role = models.CharField(max_length = 128)
  name = models.CharField(max_length = 128)
  email = models.EmailField(max_length = 128)

  def __unicode__(self):
    return self.role

class Site(models.Model):
  name = models.CharField(max_length = 128)
  url = models.URLField(max_length = 128)

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name_plural = "people"
