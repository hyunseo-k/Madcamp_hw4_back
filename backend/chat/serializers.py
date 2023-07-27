from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # 필요한 필드만 지정하거나 '__all__'로 모든 필드를 사용할 수 있습니다.

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'  # 필요한 필드만 지정하거나 '__all__'로 모든 필드를 사용할 수 있습니다.