from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import UserRole, subscription
from .models import vehicle

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['id','User_Role_Name']

class vehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicle
        fields = ['id','vehicleTypeName','capacity','size','details','price_per_km']

class subscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = subscription
        fields = ['id','sub_plan_name','price','validity_period']