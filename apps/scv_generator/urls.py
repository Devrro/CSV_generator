from django.urls import path

from apps.scv_generator.views import ListMainPage

urlpatterns = [
    path('/main', ListMainPage.as_view(), name="main_page")
]