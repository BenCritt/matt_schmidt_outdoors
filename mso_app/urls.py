from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "mso_app"

urlpatterns = [
    path("", views.index, name="home"),
    path("home/", views.index, name="home"),
    # The user will see this referred to as "/home" rather than "/index"
    # Best practice is to have the homepage HTML file named index.html
    # User experience is improved by displaying "/home" instead of "/index"
    path("about/", views.about, name="about"),
    path("events/", views.events, name="events"),
    path("our_work/", views.our_work, name="our_work"),
    path("base/", views.base, name="base"),
]

urlpatterns += staticfiles_urlpatterns()
