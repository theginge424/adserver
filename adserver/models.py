from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        app_label = 'adserver'

class Advertiser(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField()
    contact_person = models.CharField(max_length=255)
    contact_email = models.EmailField()
    registration_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    industry = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'adserver'


class Campaign(models.Model):
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    target_audience = models.ManyToManyField('Demographic', through='CampaignDemographic')
    total_budget = models.DecimalField(max_digits=12, decimal_places=2)
    remaining_budget = models.DecimalField(max_digits=12, decimal_places=2)
    goal = models.CharField(max_length=255)
    priority = models.IntegerField(choices=((1, 'Low'), (2, 'Medium'), (3, 'High')))
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'adserver'


class Ad(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag')
    pricing_model = models.ForeignKey('PricingModel', on_delete=models.PROTECT)
    landing_page_url = models.URLField(blank=True)
    view_count = models.PositiveIntegerField(default=0)
    click_count = models.PositiveIntegerField(default=0)
    approval_status = models.CharField(
        max_length=20, choices=(('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'))
    )
    creative_file = models.FileField(upload_to='ad_creatives/')
    keywords = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'adserver'


class Platform(models.Model):
    name = models.CharField(max_length=255)
    supported_formats = models.ManyToManyField('Format')
    target_locations = models.ManyToManyField('Location', through='PlatformLocation')
    daily_budget = models.DecimalField(max_digits=12, decimal_places=2)
    timezone = models.CharField(max_length=50)
    active_users = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'adserver'


class AdPlacement(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    placement_date = models.DateField()
    impressions = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)
    revenue = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Ad: {self.ad}, Platform: {self.platform}, Date: {self.placement_date}"

    class Meta:
        app_label = 'adserver'


class Demographic(models.Model):
    name = models.CharField(max_length=255)
    age_range = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    interests = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'adserver'


class CampaignDemographic(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    demographic = models.ForeignKey(Demographic, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField()

    class Meta:
        app_label = 'adserver'


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'adserver'


class Format(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'adserver'


class PricingModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cpm_rate = models.DecimalField(max_digits=10, decimal_places=2)
    cpc_rate = models.DecimalField(max_digits=10, decimal_places=2)
    cpa_rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'adserver'


class Location(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'adserver'


class PlatformLocation(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    bid_modifier = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        app_label = 'adserver'


class TargetingInterest(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'adserver'


class TargetingKeyword(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'adserver'


class TargetingPlacement(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'adserver'


# Additional models

class AdSize(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'adserver'


class AdZone(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    size = models.ForeignKey(AdSize, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'adserver'


class AdZonePlacement(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    ad_zone = models.ForeignKey(AdZone, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        app_label = 'adserver'


class AdCampaign(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Ad: {self.ad}, Campaign: {self.campaign}, Start Date: {self.start_date}"

    class Meta:
        app_label = 'adserver'
