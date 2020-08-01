from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name='test.htm'

class ThanksPage(TemplateView):
    template_name='thanks.htm'    

class HomePage(TemplateView):
    template_name='index.htm'
