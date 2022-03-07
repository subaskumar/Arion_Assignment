from rest_framework import serializers
from .model import Profile

class listingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
