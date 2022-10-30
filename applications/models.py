from email.mime import application
from multiprocessing.sharedctypes import Value
from xmlrpc.client import Fault
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from .send_tweet import send_tweet

# Create your models here.
NICHE_CHOICES = {
    ('DV', 'Developer'),
    ('AR', 'Artist'),
    ('CB', 'Community Builders'),
    ('IF', 'Influencer'),
    ('NM', 'Normie'),
    ('PF', 'Project Founder')
}
STATUS_CHOICES = {
    ('UR', 'Under Review'),
    ('AC', 'Accepted'),
    ('RJ', 'Rejected'),
    ('Wl', 'Waitlist'),
    ('NA','Not Applied')
}
TRADER_TYPE_CHOICES = {
    ('FP', 'Flipoooor'),
    ('HD', 'Holdoooor')
}
class Application(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  avatar_url = models.URLField(blank=True, null=True)
  value_to_add = models.CharField(max_length=500, null=True, blank=True)
  niche = models.CharField(choices=NICHE_CHOICES, max_length=2, blank = True, null = True)
  date_submitted = models.DateTimeField(auto_now_add=True, auto_now=False)
  wallet_address = models.CharField(max_length=100, unique = True)
  application_text = models.TextField(max_length=500)
  if_lost_followers = models.TextField(max_length=500, blank=True, null = True)
  problems_and_solution = models.TextField(max_length=500, blank=True, null = True)
  link1 = models.URLField(null= True, blank=True)
  link2 = models.URLField(null= True, blank=True, max_length=100)
  image = models.ImageField(null = True, blank = True)
  image_2 = models.ImageField(null = True, blank = True)
  image_3 = models.ImageField(null = True, blank = True)
  suggestions = models.TextField(max_length=500)
  status = models.CharField(choices=STATUS_CHOICES, max_length=2, default= 'NA')
  nft_trading_duration = models.CharField(max_length=100, null=True, blank=True)
  first_nft = models.CharField(max_length=50, null=True, blank=True)
  trader_type = models.CharField(choices=TRADER_TYPE_CHOICES, max_length=2, null=True, blank=True)
  has_been_reviewed = models.BooleanField(default= False )


  def __str__(self) -> str:
      return str(self.user.username)

  def save(self, *args, **kwargs):
    if self.status == 'AC':
        send_tweet(self.user.username, self.avatar_url)
    super(Application, self).save(*args, **kwargs)
  class Meta:
    ordering = ["-date_submitted", "user", "status"]


#   def save(self, force_insert=False, force_update=False, *args, **kwargs):





'''
def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.mode != self.__original_mode:
            #  then do this
        else:
            #  do that

        super(Mode, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_mode = self.mode
'''

'''
  def save(self, *args, **kwargs):
    if self.status == 'AP':
        send_tweet(self.user.username, self.avatar_url )
    super(Application, self).save(*args, **kwargs)

'''