from rest_framework import serializers

from .models import Event

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = ('id', 'photo', 'name',
				  'location', 'date_time', 'description')