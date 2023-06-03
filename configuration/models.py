from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Configuration(models.Model):
    split = models.IntegerField(default="1")

    def clean(self):
        if Configuration.objects.exists() and not self.pk:
            raise ValidationError(_("Only one instance of Configuration is allowed."))

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    def __str__(self):
        return "Configuration"


@receiver(post_save, sender=Configuration)
def update_settings_variable(sender, instance, **kwargs):
    from interligue import settings

    # Mettre à jour la variable dans le fichier settings
    settings.split = instance.split
