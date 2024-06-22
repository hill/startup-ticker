from uuid import uuid4

from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Startup(BaseModel):
    name = models.CharField(max_length=255)
    website = models.URLField()

    def __str__(self):
        return self.name


class TickerItem(BaseModel):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    description = models.TextField(blank=True, default="")
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    slug = models.SlugField(editable=False, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title[: min(20, len(self.title))]}")
        super().save(*args, **kwargs)


class Source(BaseModel):
    name = models.CharField(max_length=255)
    url = models.URLField()
    ticker_item = models.ForeignKey(
        TickerItem, on_delete=models.CASCADE, related_name="sources"
    )

    def __str__(self):
        return self.name
