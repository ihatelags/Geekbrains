from django.urls import path

from adminapp import views

app_name = 'adminapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-users-read/', views.UserListView.as_view(), name='admin_users_read'),
    path('admin-users-create/', views.UserCreateView.as_view(), name='admin_users_create'),
    path('admin-users-update/<int:pk>/', views.UserUpdateView.as_view(), name='admin_users_update'),
    path('admin-users-delete/<int:pk>/', views.UserDeleteView.as_view(), name='admin_users_delete'),
    path('admin_products_categories/', views.ProductCategoriesView.as_view(),
         name='admin_products_categories'),
    path('admin_products_categories/create/', views.ProductCategoriesCreateView.as_view(),
         name='admin_products_categories_create'),
    path('admin_products_categories/update/<int:pk>/',
         views.ProductCategoryUpdateView.as_view(), name='admin_products_categories_update'),
    path('admin_products_categories/remove/<int:pk>/', views.ProductCategoryDelete.as_view(),
         name='admin_products_categories_remove'),
    path('orders/read/', views.OrderListView.as_view(), name='orders'),
    path('orders/update/<int:pk>/', views.OrderUpdateView.as_view(), name='order_update'),
    path('orders/delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order_delete'),
]
