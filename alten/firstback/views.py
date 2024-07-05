from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response

from firstback.models import Product
from firstback.serializers import ProductSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the firstback index.")


@api_view(["GET"])
def hello_world(request):
    return Response({"message": "Hello, world!"})


class ProductAPIView(APIView):

    def get(self, *args, **kwargs):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
