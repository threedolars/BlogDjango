from django.db import models

# Create your models here.


class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2049)
    new_tab = models.BooleanField(default=False)

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

    def __str__(self) -> str:
        return self.title
