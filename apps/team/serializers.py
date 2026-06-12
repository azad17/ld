from rest_framework import serializers
from .models import MajorTeam
from.models import Career

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = MajorTeam
        fields = '__all__'

class CareerFilterSerializer(serializers.Serializer):
    is_active = serializers.BooleanField(required=False)
    team = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    user = serializers.CharField(required=False)
    goals = serializers.IntegerField(required=False)

class CareerFilterResponseSerializer(serializers.Serializer):
    is_active = serializers.BooleanField(
        source="user.is_active",
        read_only=True,

    )
    team = serializers.CharField(
        source='club.name',
        read_only=True
    )
    age = serializers.IntegerField(
        source ='user.age',
        read_only=True
    )
    user = serializers.CharField(
        source='user.email',
        read_only=True
    )
    class Meta:
        model = Career
        fields = [
            'user',
            'team',
            'age',
            'is_active',
            'goals'
        ]