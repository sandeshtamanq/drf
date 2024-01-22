from rest_framework import serializers

from .models import *


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):
    color = serializers.IntegerField()
    # color_info = serializers.SerializerMethodField()
    # def get_color_info(self, obj):
    #     print("obj", obj)
    #     color_obj = Color.objects.get(id=obj.color.id)
    #     return {"color_name": color_obj.color_name, "fav": False}

    class Meta:
        model = Person
        fields = "__all__"

    def validate(self, data):
        if data["age"] < 18:
            raise serializers.ValidationError("Age should be more than 18")
        return data
