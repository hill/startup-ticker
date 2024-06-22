from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Source, Startup, TickerItem


class SourceInline(admin.TabularInline):
    model = Source
    extra = 1  # Number of extra forms to display


class TickerItemAdmin(admin.ModelAdmin):
    inlines = [SourceInline]
    list_display = ("title", "pub_date", "startup", "slug_link")

    def slug_link(self, obj):
        url = reverse("item", kwargs={"slug": obj.slug})
        return format_html('<a href="{}">{}</a>', url, obj.slug)

    slug_link.short_description = "Slug"


class StartupAdmin(admin.ModelAdmin):
    list_display = ("name", "website")


admin.site.register(TickerItem, TickerItemAdmin)
admin.site.register(Startup, StartupAdmin)
