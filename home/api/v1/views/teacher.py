from rest_framework import mixins, viewsets

from home.api.v1.logic.teacher_serializer import TeacherSerializer
from home.models.teacher import Teacher


class TeacherViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Updates and retrieves teachers."""

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
