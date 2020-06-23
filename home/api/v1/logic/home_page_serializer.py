from rest_framework import serializers
from home.models.home_page import HomePage


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'
