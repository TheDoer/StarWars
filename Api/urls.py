from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views
from .views import *


urlpatterns = [

    # path('people/<peoplename>/',PeopleSearch.as_view(), name="search"),
    path('peoplepost/',PeoplePost.as_view(), name="ppost"),
    path('peopledelete/',PeopleDelete.as_view(), name="pdelete"),
    path('peopleput/',PeoplePut.as_view(), name="pput"),
    path('people/',SearchPeople.as_view(), name="peoplesearch" ),
    path('people/',PeopleView.as_view(), name="peopleget" )
]