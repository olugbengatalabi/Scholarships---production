
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("category", views.category_options, name="category_picker"),
    path("developer_applications", views.developer_form, name="developer_form"),
    path("normie_applications", views.normie_form, name="normie_form"),
    path("artist_applications", views.artist_form, name="artist_form"),
    path("founder_applications", views.founder_form, name="founder_form"),
    path("success", views.success, name="success"),
    path("builder_applications", views.builder_form, name="community_builder_form"),
    path("influencer_applications", views.influencer_form, name="influencer_form"),
    path("category_redirect", views.category_redirect, name="category_redirect"),

]

