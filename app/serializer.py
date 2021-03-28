from app.models import Songs
from rest_framework import serializers
# Create your views here.

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('id','number','title','slug','lyrics')