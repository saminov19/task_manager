from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/docs/', include('tasks.documentation_urls')), 
    # path('api/token/', include('rest_framework_simplejwt.urls', namespace='token')),
]
