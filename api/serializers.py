from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



class TokenPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(TokenPairSerializer, self).validate(attrs)
        return data

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        exclude = "last_login","is_staff","date_joined","user_permissions"



class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = "__all__"


class MultiplicatorSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        rep = super().to_representation(obj)
        rep['distributor'] = obj.distributor.username
        return rep  

    class Meta:
        model = Multiplicator
        fields = "__all__"


class VarietySerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Variety
        fields = "__all__"


class PlantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = "__all__"


class SeedSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(max_length=None, use_url=True)
    def to_representation(self, obj):
        rep = super().to_representation(obj)
        rep['plant'] = obj.plant.plant
        rep['variety'] = obj.variety.nom
        return rep  

    class Meta:
        model = Seed
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer): 
   
    class Meta:
        model = Stock
        fields = "__all__"

class AchatSerializer(serializers.ModelSerializer): 
   
    class Meta:
        model = Achat
        fields = "__all__"


class VenteSerializer(serializers.ModelSerializer): 
   
    class Meta:
        model = Vente
        fields = "__all__"