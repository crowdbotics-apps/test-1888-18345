from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.views.user import (
    SignupViewSet,
    LoginViewSet,
)
from home.api.v1.views.custom_text import CustomTextViewSet
from home.api.v1.views.home_page import HomePageViewSet
from home.api.v1.views.faculty import FacultyViewSet
from home.api.v1.views.teacher import TeacherViewSet
from home.api.v1.views.schedule import (ScheduleViewSet, ScheduleItemViewSet, ScheduleDayViewSet)


router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("teacher", TeacherViewSet)
router.register("schedule", ScheduleViewSet)
router.register("schedule-day", ScheduleDayViewSet)
router.register("schedule-item", ScheduleItemViewSet)
router.register("faculty", FacultyViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
