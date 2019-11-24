from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from stocky.views import *

router = SimpleRouter()
router.register(r'stock', StockViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('apistock/', include(router.urls)),
]
