from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from testapp.api import views
from django.conf.urls.static import static
from django.conf import settings 
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('sportsapi',views.Sports_view,basename="sports")
router.register('techapi',views.Tech_view,basename="tech")
router.register('entartainapi',views.Entertainment_view,basename="entertainment")
router.register('editorapi',views.Editorchoice_view,basename="editor")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
