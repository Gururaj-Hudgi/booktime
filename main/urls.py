from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView, RedirectView
from django.views.generic.detail import DetailView

import main.forms
import main.models
import main.views

urlpatterns = [
                  path("about-us/",
                       TemplateView.as_view(template_name="about_us.html"),
                       name='about_us'),
                  path("",
                       TemplateView.as_view(template_name="home.html"),
                       name="home"),
                  path("contact-us/",
                       main.views.ContactUs.as_view(),
                       name="contact_us"),
                  path('accounts/signup/',
                       main.views.SignupView.as_view(),
                       name="signup"),
                  path("accounts/login/",
                       auth_views.LoginView.as_view(template_name="account/login.html",
                                                    form_class=main.forms.AuthenticationForm, ),
                       name="login", ),
                  path("accounts/profile/",
                       main.views.ProfileView.as_view(),
                       name="profile", ),
                  path("products/<slug:tag>/",
                       main.views.ProductListView.as_view(),
                       name="products", ),
                  path("product/<slug:slug>/",
                       DetailView.as_view(model=main.models.Product),
                       name="product", ),
                  path(
                      "address/",
                      main.views.AddressListView.as_view(),
                      name="address_list",
                  ),
                  path(
                      "address/create/",
                      main.views.AddressCreateView.as_view(),
                      name="address_create",
                  ),
                  path(
                      "address/<int:pk>/",
                      main.views.AddressUpdateView.as_view(),
                      name="address_update",
                  ),
                  path(
                      "address/<int:pk>/delete/",
                      main.views.AddressDeleteView.as_view(),
                      name="address_delete",
                  ),
                  path(
                      "add_to_basket/",
                      main.views.add_to_basket,
                      name="add_to_basket",
                  ),
                  path('basket/',
                       main.views.manage_basket,
                       name="basket"),
                  path("accounts/", RedirectView.as_view(url='login', permanent=False)),
                  path(
                      "order/done/",
                      TemplateView.as_view(template_name="main/done_order.html"),
                      name="checkout_done",
                  ),
                  path(
                      "order/address_select/",
                      main.views.AddressSelectionView.as_view(),
                      name="address_select",
                  ),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
