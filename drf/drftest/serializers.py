from django.contrib.auth.models import User
from rest_framework import serializers
from .models import drfTest


class drfTestSerilizer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    detail=serializers.HyperlinkedIdentityField(
        view_name='drf-detail'
    )
    class Meta:
        model = drfTest
        fields =['detail','id','title','created','code','line','language','owner']


class UserSerializer(serializers.ModelSerializer):
    drftest=serializers.PrimaryKeyRelatedField(
        many=True,queryset=drfTest.objects.all()
    )
    class Meta:
        model = User
        fields = ("id", "username",'drftest')
