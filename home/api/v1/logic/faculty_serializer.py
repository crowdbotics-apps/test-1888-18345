from rest_framework import serializers

from home.models.faculty import Faculty


class FacultySerializer(serializers.ModelSerializer):
    """Faculty Serializer."""

    class Meta(object):
        model = Faculty
        fields = ('id', 'title', 'active')
