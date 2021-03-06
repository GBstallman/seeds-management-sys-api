from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings




router = routers.DefaultRouter()


router.register("client", ClientViewset)
router.register("Multiplicateur", MultiplicatorViewset)
router.register("variete", VarietyViewset)
router.register("vente", VenteViewset)
router.register("achat", AchatViewset)
router.register("user",UserViewset)
router.register("plantes", PlantViewset)
router.register("semences", SeedViewset)
router.register("stock", StockViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view())
]