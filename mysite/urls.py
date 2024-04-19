from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('home/', include('blog.urls')),
    path('user/', include('User.urls')),
]
