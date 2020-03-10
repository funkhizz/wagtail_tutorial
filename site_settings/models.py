from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    # Social media settins for website
    facebook = models.URLField(blank=True, null=True, help_text="Facebook Url")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter Url")
    youtube = models.URLField(blank=True, null=True, help_text="Youtube Url")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),
        ], heading="Social Media Settings")
    ]