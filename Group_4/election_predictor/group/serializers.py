from rest_framework import serializers
from .models import Event, Party, Group
class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('name',)


class GroupSerializer(serializers.ModelSerializer):
    admin_id=PartySerializer(read_only=True)
    class Meta:
        model = Group
        fields = ('name','admin_id')



class EventSerializer(serializers.ModelSerializer):
    group_id=GroupSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ('name', 'description', 'location', 'date','group_id')