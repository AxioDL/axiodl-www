from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View, UpdateView, DeleteView, ListView
from django.utils import timezone
from django.urls import reverse_lazy
from .forms.PageForm import PageForm
from .models import Page
from axiodl import sitesettings


class IndexView(View):

    def get(self, request, *args, **kwargs):

        if not sitesettings.is_site_locked() or (request.user.is_staff or request.user.is_superuser):
            try:
                page = Page.objects.get(is_mainpage=True)
            except ObjectDoesNotExist:
                page = None

            return render(request, 'core/index.html', {'page': page})
        else:
            return render(request, 'core/site_locked.html')


class PageView(View):

    def get(self, request, slug):

        try:
            page = Page.objects.get(slug=slug)
        except ObjectDoesNotExist:
            page = None

        return render(request, 'core/index.html', {'page': page})


class PageDeleteView(DeleteView):
    model = Page
    template_name = 'core/pages/DeletePage.html'
    success_url = reverse_lazy('home')
    slug_field = 'slug'

    def form_valid(self, form):
        page = form.save(commit=False)
        print(page)
        return self.render_to_response({'page': page})


class PageUpdateView(UpdateView):
    model = Page
    fields = ('page_name', 'description', 'content', 'logo', 'is_mainpage')
    template_name = 'core/pages/NewEditPage.html'
    context_object_name = 'page'
    slug_field = 'slug'

    def form_valid(self, form):
        page = form.save(commit=False)
        page.updated_by = self.request.user
        page.updated_at = timezone.now()
        page.save()
        return redirect('pages.view.page', slug=page.slug)


class PageListView(ListView):
    model = Page
    template_name = 'core/pages/ListPages.html'


@permission_required('core.add_page')
def create_page(request):
    if request.method == 'POST':
        if 'cancel' in request.POST:
            return redirect('home')

        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            page = form.save(commit=False)
            page.created_by = request.user
            page.save()

            return redirect('home')
    else:
        form = PageForm()
    return render(request, 'core/pages/NewEditPage.html', {'form': form})
