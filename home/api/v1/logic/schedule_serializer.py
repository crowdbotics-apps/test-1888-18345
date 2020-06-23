# -*- coding: utf-8 -*-
from rest_framework import serializers

from home.models.schedule import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    """Schedule model serializer."""

    faculty_title = serializers.SerializerMethodField(required=False)

    def get_faculty_title(self, obj):
        """Faculty name."""
        return obj.faculty.title

    class Meta(object):
        model = Schedule
        fields = ('id', 'title', 'faculty', 'faculty_title', 'year', 'term', 'education_format')

