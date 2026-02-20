from .forms import CarFilterForm

class CarFilterMixin:
    filter_form_class = CarFilterForm
    filter_available_only = False

    def get_queryset(self):
        qs = super().get_queryset()

        if self.filter_available_only or self.request.GET.get('available') == '1':
            qs = qs.filter(is_available=True)

        form = self.filter_form_class(self.request.GET)
        if form.is_valid():
            brand = form.cleaned_data.get('brand')
            sort = form.cleaned_data.get('sort')

            if brand:
                qs = qs.filter(brand__name__icontains=brand)
            if sort == 'price':
                qs = qs.order_by('price_per_day')
            elif sort == 'year':
                qs = qs.order_by('-year')

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = self.filter_form_class(self.request.GET)
        context['available_only'] = self.filter_available_only or self.request.GET.get('available') == '1'
        return context