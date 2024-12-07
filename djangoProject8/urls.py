"""
URL configuration for djangoProject8 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from capital import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view_stock/stock', views.view_stock, name='view_stock'),
    path('stocks/issue/<int:stocks_id>', views.issue, name='issue'),
    path('stocks/return_product/<int:stocks_id>', views.return_product, name='return_product'),
    path('stocks/details/<int:stocks_id>', views.product_details, name='product_details'),
    path('add_stock/stock', views.add_stock, name='add_stock'),
     path('history/', views.history, name='history'),
    path('login', views.login_user, name='login'),
    path('logout', views.signout_user, name='logout'),

    path('stocks/delete/<int:stocks_id>', views.delete_product, name='delete_product'),
    path('stock/search', views.search_product, name='search_product'),
    path('purchase/delete/<int:purchase_id>', views.delete_purchase, name='delete_purchase'),
    path('admin/', admin.site.urls),
]
