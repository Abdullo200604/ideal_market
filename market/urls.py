from django.urls import path
from . import views

urlpatterns = [

    # 🌐 Bosh sahifa va Kassa
    path('', views.home, name='home'),
    path('kassa/', views.kassa, name='kassa'),

    # 🛒 Savat funksiyalari
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
    path('cart/checkout/', views.cart_checkout, name='cart_checkout'),
    path('cart/update/<int:product_id>/', views.cart_update, name='cart_update'),

    # 🧾 Cheklar (Sales history)
    path('cheklar/', views.sales_list, name='sales_list'),
    path('cheklar/<int:pk>/', views.sale_detail, name='sale_detail'),
    path('cheklar/export/pdf/', views.export_sales_pdf, name='export_sales_pdf'),

    # 📊 Statistika
    path('statistika/', views.statistics, name='statistics'),
    path('statistics/export/excel/', views.export_statistics_excel, name='statistics_export_excel'),
    path('statistics/export/pdf/', views.export_statistics_pdf, name='statistics_export_pdf'),

    # ⚙️ Admin boshqaruv paneli
    path('management/', views.admin_management, name='admin_management'),

    # 📦 Mahsulotlar boshqaruvi
    path('management/products/', views.admin_products, name='admin_products'),
    path('management/products/add/', views.admin_product_add, name='admin_product_add'),
    path('management/products/edit/<int:pk>/', views.admin_product_edit, name='admin_product_edit'),
    path('management/products/delete/<int:pk>/', views.admin_product_delete, name='admin_product_delete'),
    path('management/products/bulk_delete/', views.admin_product_bulk_delete, name='admin_product_bulk_delete'),
    path('management/products/import/', views.management_product_import, name='management_product_import'),
    path('management/products/export/', views.management_product_export, name='management_product_export'),


    # 👤 Foydalanuvchilar boshqaruvi
    path('management/users/', views.admin_users, name='admin_users'),
    path('management/users/add/', views.admin_user_add, name='admin_user_add'),
    path('management/users/<int:user_id>/edit/', views.admin_user_edit, name='admin_user_edit'),
    path('management/users/<int:user_id>/delete/', views.admin_user_delete, name='admin_user_delete'),

    # 👥 Guruhlar boshqaruvi
    path('management/groups/', views.admin_groups, name='admin_groups'),
    path('management/groups/add/', views.admin_group_add, name='admin_group_add'),
    path('management/groups/<int:group_id>/edit/', views.admin_group_edit, name='admin_group_edit'),
    path('management/groups/<int:group_id>/delete/', views.admin_group_delete, name='admin_group_delete'),

    # 💰 Sotuvlar boshqaruvi
    path('management/sales/', views.admin_sales, name='admin_sales'),
    path('management/sales/<int:sale_id>/', views.admin_sale_detail, name='admin_sale_detail'),
    path('management/sales/<int:sale_id>/delete/', views.admin_sale_delete, name='admin_sale_delete'),

    # Foydalanuvchi parolini o‘zgartirish
    path('management/users/<int:user_id>/change_password/', views.admin_user_change_password, name='admin_user_change_password'),

]
