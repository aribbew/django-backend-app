from rest_framework.routers import DefaultRouter

from products.api.views import ProductApiViewset

router_product = DefaultRouter()

router_product.register(
    prefix='products', basename='products', viewset=ProductApiViewset
)
