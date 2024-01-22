from django.urls import include, path
from rest_framework.routers import DefaultRouter

from home.views import PeopleViewSet, PersonView, index, login, people, single_people

router = DefaultRouter()
router.register(r"people", PeopleViewSet, basename="people")
urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
    path("index/", index),
    path("person/", people),
    path("person/<id>/", single_people),
    path("login/", login),
    path("peoples/", PersonView.as_view()),
]
