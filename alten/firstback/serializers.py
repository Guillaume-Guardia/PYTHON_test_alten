from rest_framework.serializers import ModelSerializer

from firstback.models import Product


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "name"]
