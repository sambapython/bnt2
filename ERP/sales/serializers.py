from rest_framework import serializers
from sales.models import Customer
class CustomerSerializer(serializers.ModelSerializer):
 	class Meta:
 		model = Customer
 		fields="__all__"

 	def validate_name(self, value):
 		if not value.isalnum():
 			raise serializers.ValidationErrror("Expecting only alphanumeric")
 		return value

class CustomerGetSerializer(serializers.ModelSerializer):
 	class Meta:
 		model = Customer
 		fields=["name","gender"]