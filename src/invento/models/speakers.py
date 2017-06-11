from django.db import models

from users.models import UserProfile


class Speaker(models.Model):
    profile = models.OneToOneField(UserProfile, db_index=True)
    about = models.TextField(max_length=500, blank=True, null=True)
    avatar = models.URLField(max_length=200, unique=True, blank=True,
                             null=True)

    class Meta:
        db_table = 'speakers'
