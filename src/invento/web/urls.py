from __future__ import absolute_import

from django.conf.urls import url

# internal imports
from invento.web.frontend.home import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(),
        name='invento'),
]
