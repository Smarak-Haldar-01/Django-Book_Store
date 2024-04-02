"""
URL configuration for Book_Store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include,path
from Book_Store import views
from Users import views as view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin-redirect/", admin.site.urls),
    path("",views.index,name='home'),
    path("login/",views.log_in,name='login'),
    path("logout/",views.logout,name='logout'),
    path("signin/",views.signin,name='signin'),
    path("error/",views.error,name='error'),
    path("add_pr$o#duct/<int:id>",views.manager_add_product,name='add_product'),
    path("private_home/<int:id>",views.private_index,name='m_home'),
    path('deletes/<int:mid>/<int:pid>',views.deletes,name='deletes'),
    path('view_products/<int:id>',views.productView,name='view_products'),
    path('orders/<int:id>',views.orders,name='orders'),
    path('user_control/<int:id>',views.user_index,name='home_u'),
    path('view-order/<int:id>',views.viewOrder,name="view_order"),
    path('deleteUser/<int:id>',views.deleteUser,name='deleteUser'),
    path('report_problem/<int:id>',views.report_problem_u,name='report_p_u'),
    path('reported_problems/<int:id>',views.reported_problems,name='reported-m'),
    path('help-line/',views.helpLine,name='helpline'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)