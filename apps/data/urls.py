from django.urls import include, path
from rest_framework.routers import DefaultRouter

from rest_framework_nested import routers

from . import views

router = DefaultRouter()
router.register(r"suppliers", views.SupplierViewSet, base_name="suppliers")
router.register(r"products", views.ProductViewSet, base_name="products")
router.register(r"items", views.ItemViewSet, base_name="items")
router.register(r"orders", views.OrderViewSet, base_name="orderms")

suppliers_router = routers.NestedSimpleRouter(router, r"suppliers", lookup="supplier")
suppliers_router.register(r"products", views.SProductViewSet, base_name="supplier-products")

urlpatterns = [path("", include(router.urls)), path("", include(suppliers_router.urls))]
