from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import View
from .models import Ad, Campaign, Advertiser, Platform, Format, PricingModel, AdPlacement
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'user': user,
        'profile': profile,
        'form': form,
    }

    return render(request, 'adserver/profile.html', context)

def home(request):
    ads = Ad.objects.all()
    campaigns = Campaign.objects.all()
    advertisers = Advertiser.objects.all()
    platforms = Platform.objects.all()
    formats = Format.objects.all()
    pricing_models = PricingModel.objects.all()
    ad_placements = AdPlacement.objects.all()

    context = {
        'ads': ads,
        'campaigns': campaigns,
        'advertisers': advertisers,
        'platforms': platforms,
        'formats': formats,
        'pricing_models': pricing_models,
        'ad_placements': ad_placements,
    }

    return render(request, 'adserver/home.html', context)

class HomeView(View):
    template_name = 'registration.html'

    def get(self, request):
        # Logic to fetch data if needed
        return render(request, self.template_name)



class UserRegistrationView(View):
    template_name = 'registration.html'

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the user registration data to the database
            user_id = form.cleaned_data['user_id']
            user_name = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            # Save the user to the database using your preferred method
            # Example: user = User.objects.create(user_id=user_id, user_name=user_name, email=email, password=password)
            return redirect('profile')  # Replace 'profile' with the desired URL after registration

        return render(request, self.template_name, {'form': form})


class AdListView(View):
    def get(self, request):
        ads = Ad.objects.all()
        # Logic to retrieve and process data for the ad list page
        # Render the template with the retrieved data and return the response
        return render(request, 'ad_list.html', {'ads': ads})

class AdDetailView(View):
    def get(self, request, pk):
        ad = get_object_or_404(Ad, pk=pk)
        # Logic to retrieve and process data for the ad detail page
        # Render the template with the retrieved data and return the response
        return render(request, 'ad_detail.html', {'ad': ad})

class CampaignListView(View):
    def get(self, request):
        campaigns = Campaign.objects.all()
        # Logic to retrieve and process data for the campaign list page
        # Render the template with the retrieved data and return the response
        return render(request, 'campaign_list.html', {'campaigns': campaigns})

class CampaignDetailView(View):
    def get(self, request, pk):
        campaign = get_object_or_404(Campaign, pk=pk)
        # Logic to retrieve and process data for the campaign detail page
        # Render the template with the retrieved data and return the response
        return render(request, 'campaign_detail.html', {'campaign': campaign})

class AdvertiserListView(View):
    def get(self, request):
        advertisers = Advertiser.objects.all()
        # Logic to retrieve and process data for the advertiser list page
        # Render the template with the retrieved data and return the response
        return render(request, 'advertiser_list.html', {'advertisers': advertisers})

class AdvertiserDetailView(View):
    def get(self, request, pk):
        advertiser = get_object_or_404(Advertiser, pk=pk)
        # Logic to retrieve and process data for the advertiser detail page
        # Render the template with the retrieved data and return the response
        return render(request, 'advertiser_detail.html', {'advertiser': advertiser})

class PlatformListView(View):
    def get(self, request):
        platforms = Platform.objects.all()
        # Logic to retrieve and process data for the platform list page
        # Render the template with the retrieved data and return the response
        return render(request, 'platform_list.html', {'platforms': platforms})

class PlatformDetailView(View):
    def get(self, request, pk):
        platform = get_object_or_404(Platform, pk=pk)
        # Logic to retrieve and process data for the platform detail page
        # Render the template with the retrieved data and return the response
        return render(request, 'platform_detail.html', {'platform': platform})

class FormatListView(View):
    def get(self, request):
        formats = Format.objects.all()
        # Logic to retrieve and process data for the format list page
        # Render the template with the retrieved data and return the response
        return render(request, 'format_list.html', {'formats': formats})

class FormatDetailView(View):
    def get(self, request, pk):
        format = get_object_or_404(Format, pk=pk)
        # Logic to retrieve and process data for the format detail page
        # Render the template with the retrieved data and return the response
        return render(request, 'format_detail.html', {'format': format})

class PricingModelListView(View):
    def get(self, request):
        pricing_models = PricingModel.objects.all()
        # Logic to retrieve and process data for the pricing model list page
        # Render the template with the retrieved data and return the response
        return render(request, 'pricing_model_list.html', {'pricing_models': pricing_models})

class PricingModelDetailView(View):
    def get(self, request, pk):
        pricing_model = get_object_or_404(PricingModel, pk=pk)
        # Logic to retrieve and process data for the pricing model detail page
        # Render the template with the retrieved data and return the response
        return render(request, 'pricing_model_detail.html', {'pricing_model': pricing_model})

class AdPlacementListView(View):
    def get(self, request):
        ad_placements = AdPlacement.objects.all()
        # Logic to retrieve and process data for the ad placement list page
        # Render the template with the retrieved data and return the response
        return render(request, 'ad_placement_list.html', {'ad_placements': ad_placements})

class AdPlacementDetailView(View):
    def get(self, request, pk):
        ad_placement = get_object_or_404(AdPlacement, pk=pk)
        # Logic to retrieve and process data for the ad placement detail page
        # Render the template with the retrieved data and return the response
        return render(request, 'ad_placement_detail.html', {'ad_placement': ad_placement})
    
    
