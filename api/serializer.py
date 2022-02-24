from rest_framework import  serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    """ Serialozer user
    """  

    class Meta:
        model = models.User
        fields = '__all__'

class PrizeSerializer(serializers.ModelSerializer):
    """ Serialozer prize
    """  

    class Meta:
        model = models.Prize
        fields = ('code', 'perday', 'name')



class ConcorsoSerializer(serializers.ModelSerializer):
    """ Serialozer concorso
    """  
   
    class Meta:
        model = models.Concorso
        fields = ('id', 'code', 'name', 'start', 'end', 'prize', 'user')

class ConcorsoListSerializer(ConcorsoSerializer):
    """ Serialozer concorso list
    """  
    prize = PrizeSerializer()
    user = UserSerializer(many=True, read_only=True)

class WinerSerializer(serializers.ModelSerializer):
    """ Serialozer winer
    """  
    class Meta:
        model = models.Winer
        fields = '__all__'

class GoogleAuth(serializers.Serializer):
    """ danni from google"""
    email = serializers.EmailField()
    token = serializers.CharField()

