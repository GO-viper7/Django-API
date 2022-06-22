from unittest.util import _MAX_LENGTH
from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    year = serializers.IntegerField()