from rest_framework import serializers


class HelloSerlializer(serializers.Serializer):
    """selializes a name field for testing our ApiViews"""
    name = serializers.CharField(max_length=10)

