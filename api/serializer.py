from rest_framework import serializers

from modelapp.models import Users, Notes


class Userserialiser(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Users


class Noteserialiser(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Notes
