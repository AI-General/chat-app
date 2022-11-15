from rest_framework import serializers

from .models import Room, Chat

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room 
        fields = ("id","room_name","room_code")
        lookup_field = "room_code"

class ChatSerializer(serializers.ModelSerializer):
    from_user = serializers.CharField(source="from_user.username")

    class Meta:
        model = Chat 
        fields = '__all__'
        read_only_fields = ['room', 'from_user', 'text']

        extra_kwargs = {k: {'read_only':True} for k in read_only_fields}