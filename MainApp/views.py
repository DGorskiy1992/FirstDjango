from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


def item_page(request, id):
    try:
        item = Item.objects.get(pk=id)
        context = {"item": item}
        return render(request, "item.html", context)
    except ObjectDoesNotExist:
        raise Http404(f"Товар с id={id} не найден!")


def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items.html", context)


def home(request):
    return render(request, "index.html")


def page1(request):
    return render(request, "page1.html")