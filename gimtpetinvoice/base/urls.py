
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('invoicing.urls')),
    path('provider/', include('provider.urls'))
]
