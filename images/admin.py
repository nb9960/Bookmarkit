from django.contrib import admin
from .models import Image
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']
<<<<<<< HEAD

=======
>>>>>>> ee48f05ab9280e740225c4db22159baa7feafcc9
