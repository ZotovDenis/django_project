from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from materials.models import Material


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'content', 'preview', 'created_date', 'is_published')
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        """Создание slug name"""
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', 'content', 'preview', 'created_date', 'is_published')
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        """Создание slug name"""
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        """Перенаправление на просмотр статьи после редактирования"""
        return reverse('materials:view', args=[self.kwargs.get('pk')])


class MaterialListView(ListView):
    model = Material

    def get_queryset(self, *args, **kwargs):
        """Отображение только активных статей"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class MaterialDetailView(DetailView):
    model = Material

    def get_object(self, queryset=None):
        """Счетчик просмотров статьи"""
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('materials:list')
