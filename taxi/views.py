from django.shortcuts import render
from django.views import generic

from taxi.models import Driver, Car, Manufacturer


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturers"
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    context_object_name = "cars"
    queryset = Car.objects.select_related("manufacturer")
    paginate_by = 5


class CarDetailView(generic.DetailView):
    model = Car


class DriverListView(generic.ListView):
    model = Driver
    context_object_name = "drivers"
    paginate_by = 5


class DriverDetailView(generic.DetailView):
    model = Driver
