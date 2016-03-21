from rest_framework import serializers

from .models import Travel

class TravelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Travel
		fields = ('id', 'title', 'origin',
				  'destination', 'depart_date', 'return_date')