from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("teams",views.TeamViewSet,basename='teams')


urlpatterns = [
    path("careerfilter",views.CareerFilterView.as_view(),name='career-filter'),
    path("weather",views.WeatherCheck.as_view(),name="weather"),
     path("weather2",views.weather,name="weather2")
]
urlpatterns += router.urls