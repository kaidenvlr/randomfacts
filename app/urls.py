from app.views import FactsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', FactsViewSet, basename='fact')

urlpatterns = router.urls
