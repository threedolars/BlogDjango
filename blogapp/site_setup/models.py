# flake8: noqa
from collections.abc import Iterable
from django.db import models
from utils.modelvalidator import validate_image
from utils.redimensionator import rezize_image

# Create your models here.


class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2049)
    new_tab = models.BooleanField(default=False)
    # Relationship one-to-many
    site_setup = models.ForeignKey('SiteSetup', on_delete=models.CASCADE,
                                   blank=True, null=True, default=None)

    def __str__(self):
        return self.text


class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'

    title = models.CharField(max_length=66)
    description = models.CharField(max_length=250)

    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)

    favicon = models.ImageField(upload_to='assets/favicon/%Y/%m/',
                                blank=True, default='', validators=[validate_image])

    def save(self, *args, **kwargs):
        current_favicon_name = str(self.favicon.name)
        super().save(*args, **kwargs)
        favicon_changed = False

        if self.favicon:
            favicon_changed = current_favicon_name != self.favicon.name

        if favicon_changed:
            rezize_image(self.favicon, 32)

    def __str__(self) -> str:
        return self.title
