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

# use the Python urllib module to download the image and then call the save() method of the image field, 
# passing it a ContentFile object that is instantiated with the downloaded file content.
# pass the save=False parameter to avoid saving the object to the database yet.
# to use the urllib to retrieve images from URLs served through HTTPS,install the Certifi Python package. 
# Certifi is a collection of root certificates for validating the trustworthiness of SSL/TLS certificates.    
# Install certifi with the following command: pip3 install --upgrade certifi

# will allow users to bookmark images from external websites. 
# The user will provide the URL of the image, a title, and an optional description.
# application will download the image and create a new Image object in the database


# Users will not enter the image URL directly in the form.
# Instead, will provide them with a JavaScript tool to choose an image from an external site,
# and form will receive its URL as a parameter.
# WE override the default widget of the url field to use a HiddenInput widget.
# This widget is rendered as an HTML input element with a type="hidden" attribute. 
# We use this widget because you don't want this field to be visible to users.