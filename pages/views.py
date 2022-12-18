from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/my_account.html"


class HomePage(TemplateView):
    template_name = "pages/home.html"

class FilePage(TemplateView):
    template_name = "pages/files.html"

