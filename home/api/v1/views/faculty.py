from rest_framework import mixins, viewsets

from home.api.v1.logic.faculty_serializer import FacultySerializer
from home.models.faculty import Faculty


class FacultyViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Updates and retrieves faculty."""

    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
