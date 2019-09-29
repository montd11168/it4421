from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_nested import routers

router = DefaultRouter()
router.register(r"suppliers", views.SupplierViewSet)

suppliers_router = routers.NestedSimpleRouter(router, r'suppliers', lookup='supplier')
suppliers_router.register(r'products', views.ProductViewSet, base_name='supplier-products')

urlpatterns = [path("", include(router.urls)), path("", include(suppliers_router.urls))]
