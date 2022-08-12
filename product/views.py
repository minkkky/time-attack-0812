from itertools import product
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Product, SubscribeLog
from .serializers import ProductSerializer

# Create your views here.
class ProductView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        products = Product.objects.filter(active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, product_id):
        return