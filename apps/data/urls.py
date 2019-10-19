from django.urls import include, path
from rest_framework.routers import DefaultRouter

from rest_framework_nested import routers

from . import views

router = DefaultRouter()
router.register(r"suppliers", views.SupplierViewSet, base_name="suppliers")
router.register(r"products", views.ProductViewSet, base_name="products")
router.register(r"items", views.ItemViewSet, base_name="items")
router.register(r"orders", views.OrderViewSet, base_name="orders")

suppliers_router = routers.NestedSimpleRouter(router, r"suppliers", lookup="supplier")
suppliers_router.register(r"products", views.SProductViewSet, base_name="supplier-products")

products_router = routers.NestedSimpleRouter(router, r"products", lookup="product")
products_router.register(r"comments", views.CommentViewSet, base_name="product-comments")
products_router.register(r"votes", views.VoteViewSet, base_name="product-votes")
products_router.register(r"images", views.ImageViewSet, base_name="product-images")
products_router.register(r"colors", views.ColorViewSet, base_name="product-colors")

urlpatterns = [
    path("", include(router.urls)), 
    path("", include(suppliers_router.urls)), 
    path("", include(products_router.urls)),
]
