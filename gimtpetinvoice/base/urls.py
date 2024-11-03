
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('provider/', include('provider.urls')),
    path('invoicing/', include('invoicing.urls'))
]
