from django.conf.urls import url
from . import views
app_name = 'images'
urlpatterns = [
    url(r'^create/', views.image_create, name='create'),
    url(r'^detail/<int:id>/<slug:slug>/',
     views.image_detail, name='detail'),
    url(r'^like/', views.image_like, name='like'),
    url(r'^$', views.image_list, name='list'),
    url(r'^ranking/', views.image_ranking, name='ranking'),
]
