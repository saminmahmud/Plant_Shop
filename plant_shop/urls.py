
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plant/', include('plant.urls')),
    path('order/', include('order.urls')),
    path('category/', include('category.urls')),
    path('account/', include('account.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
