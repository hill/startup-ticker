from django.shortcuts import get_object_or_404, render

from ticker.models import TickerItem


def index(request):
    items = TickerItem.objects.all()
    return render(request, "index.html", {"items": items})


def item(request, slug: str):
    item = get_object_or_404(TickerItem.objects.select_related("startup"), slug=slug)
    return render(request, "item.html", {"item": item})
