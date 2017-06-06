from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, db_index=True)
    mobile = models.CharField(max_length=20, unique=True)
    address = models.TextField(max_length=500, blank=True, null=True)
    facebook_handle = models.CharField(max_length=50, blank=True, null=True,
                                       unique=True)
    twitter_handler = models.CharField(max_length=50, blank=True, null=True,
                                       unique=True)
    googleplus_handle = models.CharField(max_length=50, blank=True, null=True,
                                         unique=True)

    class Meta:
        db_table = 'user_profiles'
