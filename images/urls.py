from django.conf.urls import url
from . import views
app_name = 'images'
urlpatterns = [
    url(r'^create/', views.image_create, name='create'),
<<<<<<< HEAD
]
=======
]
>>>>>>> ee48f05ab9280e740225c4db22159baa7feafcc9
