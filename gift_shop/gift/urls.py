from django.urls import path, include
from gift import views
from .views import ProductDetail, search_products

# urlpatterns = [
#     path('latest-products/', views.LatestProductsList.as_view(), name='latest-products'), 
#     path('api/v1/products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view(), name='product-detail'), 
#     ]

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view(), name='latest-products'), 
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    # path('products/search', views.search),
    path('products/search', search_products, name='search_products'),
    # path('products/search/', ProductSearchView.as_view()),
]

