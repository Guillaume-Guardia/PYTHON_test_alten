from django.urls import path, include
from rest_framework import routers
from .views import ProductViewset

router = routers.SimpleRouter()
router.register("products", ProductViewset, basename="product")

urlpatterns = [
    path("", include(router.urls)),
]
