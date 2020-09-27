from rest_framework import serializers
from profiles_api import models


class HelloSerlializer(serializers.Serializer):
    """selializes a name field for testing our ApiViews"""
    name = serializers.CharField(max_length=10)


class UserProfileSerilalizer(serializers.ModelSerializer):
    """Serliaizes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}  # when user enters password it's will showing a dots inside inputs

            }
        }

    def create(self, validated_data):
        """Create and return a new User"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name']
        )
        return user
