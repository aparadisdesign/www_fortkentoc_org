from django.urls import path
from django.views.generic import TemplateView

app_name = "website"

urlpatterns = [
    path('', TemplateView.as_view(template_name="website/home.html"), name="home"),
    path('about-us', TemplateView.as_view(template_name="website/about_us/about_us.html"), name="about_us"),
    path('facilities', TemplateView.as_view(template_name="website/about_us/facilities.html"), name="facilities"),
    path('trails', TemplateView.as_view(template_name="website/about_us/trails.html"), name="trails"),
    path('policies-and-safety', TemplateView.as_view(template_name="website/about_us/policies_and_safety.html"), name="policies_and_safety"),
    path('programs', TemplateView.as_view(template_name="website/about_us/programs.html"), name="programs"),
]
