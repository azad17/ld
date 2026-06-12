from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register("department",views.DepartmentViewSet,basename='department')

urlpatterns = [
path("",views.HomeView.as_view(),name='home'),
path("department",views.DepartmentCreateView.as_view(),name='department')
]

# urlpatterns+=router.urls