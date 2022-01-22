import requests
from decouple import config
from django.views.generic import TemplateView

GROOM_EASE_LOGIN_DATA = {
    "username": config("GROOM_EASE_USER"),
    "password": config("GROOM_EASE_PASS")
}


class HomeView(TemplateView):
    template_name = "website/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = GROOM_EASE_LOGIN_DATA
        r = requests.post('https://api.groomease.app/auth/jwt/login', data=data, headers=headers)
        if r.status_code == 200:
            response = r.json()
            headers = {
                "Authorization": f"Bearer {response.get('access_token')}",
                "Content-Type": "application/json"
            }
            r = requests.get('https://api.groomease.app/users/me/trail-systems', headers=headers)
            if r.status_code == 200:
                context['trail_systems'] = r.json()
        return context