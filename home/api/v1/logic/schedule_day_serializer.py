# -*- coding: utf-8 -*-
from rest_framework import serializers

from home.models.schedule_day import ScheduleDay


class ScheduleDaySerializer(serializers.ModelSerializer):
    """ScheduleDay Serializer."""

    class Meta(object):
        model = ScheduleDay
        fields = ('id', 'title', 'date', 'schedule')
