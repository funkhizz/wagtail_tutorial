from django.db import models

class Subscriber(models.Model):
    email = models.CharField(max_length=40, blank=False, null=False, help_text="Email address")
    full_name = models.CharField(max_length=100, blank=False, null=False, help_text="First+Last Name")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Subscribers"
        verbose_name_plural = "Subscribers"