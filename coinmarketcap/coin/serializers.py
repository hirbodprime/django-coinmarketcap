from rest_framework.serializers import ModelSerializer
from .models import CoinDataModel
class CoinsListApiSerializer(ModelSerializer):
    class Meta:
        model= CoinDataModel
        fields = '__all__'