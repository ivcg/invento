from django.db import models


class Organization(models.Model):
    """
    An organization holding events.
    """
    name = models.CharField(max_length=200, db_index=True, unique=True)
    description = models.TextField(max_length=1000)
    website = models.URLField(max_length=200)
    cover_image = models.FileField(max_length=200, allow_empty_file=True)
    address = models.TextField(max_length=1000, blank=True, null=True)
    github_handle = models.CharField(max_length=50, blank=True, null=True,
                                     unique=True)
    facebook_handle = models.CharField(max_length=50, blank=True, null=True,
                                       unique=True)
    twitter_handler = models.CharField(max_length=50, blank=True, null=True,
                                       unique=True)
    googleplus_handle = models.CharField(max_length=50, blank=True, null=True,
                                         unique=True)

    class Meta:
        db_table = 'organizations'

# TODO
# OrganizationAdmins
