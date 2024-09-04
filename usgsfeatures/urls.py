from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sidebarquery.urls')),
    path('authenticate/', include('authenticate.urls')),
    path('payments/', include('payments.urls')),
    path('bookmarks/', include('bookmarks.urls')),
]

