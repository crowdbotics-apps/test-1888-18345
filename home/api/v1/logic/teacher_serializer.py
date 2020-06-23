from rest_framework import serializers

from home.models.teacher import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    """Teacher Serializer."""

    class Meta(object):
        model = Teacher
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'teaching_subject', 'active')
