from django.urls import path

from . import views

app_name = 'weather'
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("privacyPolicy/", views.policy, name="policy"),
    path("termsAndconditions/", views.terms, name="terms"),
    path("blog/dialogFlowToGoogleSheets/", views.dfgs, name="dfgs"),
    path("search/", views.search, name="search"),
    path("contactMe/", views.contactMe, name="contactMe"),
    path("contactMe/contact-redirect-success/", views.contactSuccess, name="contactSuccess"),
    path("contactMe/contact-redirect-error/", views.contactError, name="contactError"),
]