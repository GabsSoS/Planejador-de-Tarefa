
from django.contrib import admin
from django.urls import path
from planer.views import PlanerCreateListView, PlanerRetriveUpdateDestroyerView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('planer-list/', PlanerCreateListView.as_view(), name='planer-list'),
    path('planer/<int:pk>', PlanerRetriveUpdateDestroyerView.as_view(), name='planer-detail'),
]