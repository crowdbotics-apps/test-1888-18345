from rest_framework import exceptions, mixins, viewsets
from rest_framework.permissions import AllowAny

from home.api.v1.logic.schedule_day_serializer import ScheduleDaySerializer
from home.api.v1.logic.schedule_item_serializer import (
    ScheduleItemCreateSerializer,
    ScheduleItemSerializer,
    ScheduleItemUpdateSerializer,
)
from home.api.v1.logic.schedule_serializer import ScheduleSerializer
from home.models.schedule import Schedule
from home.models.schedule_day import ScheduleDay
from home.models.schedule_item import ScheduleItem


class ScheduleViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Updates and retrieves schedules."""

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleDayViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Updates and retrieves schedules for a day."""

    queryset = ScheduleDay.objects.all()
    serializer_class = ScheduleDaySerializer


class ScheduleItemViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Updates and retrieves schedule items."""

    queryset = ScheduleItem.objects.all()
    serializer_class = ScheduleItemSerializer

    def get_serializer(self, *args, **kwargs):
        """
        Route serializers based on action.

            list                    ScheduleItemSerializer
            retrieve                ScheduleItemSerializer
            update, partial_update  ScheduleItemUpdateSerializer
            create                  ScheduleItemCreateSerializer
        """
        if self.request.user.is_anonymous and AllowAny in self.permission_classes:
            kwargs['context'] = self.get_serializer_context()
            return self.serializer_class(*args, **kwargs)
        if self.action in {'list', 'retrieve'}:
            serializer_class = ScheduleItemSerializer
        elif self.action in {'update', 'partial_update'}:
            serializer_class = ScheduleItemUpdateSerializer
        elif self.action == 'create':
            serializer_class = ScheduleItemCreateSerializer
        else:
            serializer_class = None

        if serializer_class is None:
            raise exceptions.ValidationError(detail={self.action: ['Permission error.']})
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
