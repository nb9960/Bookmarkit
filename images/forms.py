from django import forms
from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify
class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not ' \
                                        'match valid image extensions.')
        return url

    def save(self, force_insert=False,
                force_update=False,
                commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        # download image from the given URL
        response = request.urlopen(image_url)
        image.image.save(image_name,
                        ContentFile(response.read()),
                        save=False)
        if commit:
            image.save()
        return image

# use the Python urllib module to download the image and then call the save() method of the image field, passing it a ContentFile object that is instantiated with the downloaded file content. In this way, you save the file to the media directory of your project. You pass the save=False parameter to avoid saving the object to the database yet.
# In order to use the urllib to retrieve images from URLs served through HTTPS, you need to install the Certifi Python package. Certifi is a collection of root certificates for validating the trustworthiness of SSL/TLS certificates.    Install certifi with the following command:
# pip3 install --upgrade certifi
