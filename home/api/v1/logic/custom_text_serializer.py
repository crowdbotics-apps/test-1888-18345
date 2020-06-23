from rest_framework import serializers
from home.models.custom_text import CustomText


class CustomTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomText
        fields = '__all__'