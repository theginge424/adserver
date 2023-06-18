from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views  # Import the views module

from adserver.views import (
    HomeView,
    AdListView,
    AdDetailView,
    CampaignListView,
    CampaignDetailView,
    AdvertiserListView,
    AdvertiserDetailView,
    PlatformListView,
    PlatformDetailView,
    FormatListView,
    FormatDetailView,
    PricingModelListView,
    PricingModelDetailView,
    AdPlacementListView,
    AdPlacementDetailView,
    UserRegistrationView,
)

app_name = 'adserver'

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/register/', UserRegistrationView.as_view(), name='register'),
    path('admin/', admin.site.urls),
    path('ads/', AdListView.as_view(), name='ad_list'),
    path('ads/<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('advertisers/', AdvertiserListView.as_view(), name='advertiser_list'),
    path('advertisers/<int:pk>/', AdvertiserDetailView.as_view(), name='advertiser_detail'),
    path('ad_placements/', AdPlacementListView.as_view(), name='ad_placement_list'),
    path('ad_placements/<int:pk>/', AdPlacementDetailView.as_view(), name='ad_placement_detail'),
    path('campaigns/', CampaignListView.as_view(), name='campaign_list'),
    path('campaigns/<int:pk>/', CampaignDetailView.as_view(), name='campaign_detail'),
    path('formats/', FormatListView.as_view(), name='format_list'),
    path('formats/<int:pk>/', FormatDetailView.as_view(), name='format_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='adserver/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('platforms/', PlatformListView.as_view(), name='platform_list'),
    path('platforms/<int:pk>/', PlatformDetailView.as_view(), name='platform_detail'),
    path('pricing_models/', PricingModelListView.as_view(), name='pricing_model_list'),
    path('pricing_models/<int:pk>/', PricingModelDetailView.as_view(), name='pricing_model_detail'),
]

# Add the registration URL pattern
urlpatterns += [
    path('registration/', include('adserver.urls', namespace='registration')),
]
