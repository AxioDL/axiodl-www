from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import UpdateView
from django.utils import timezone
from .forms.PageForm import PageForm
from .models import Page


def index(request):
    try:
        page = Page.objects.get(is_mainpage=True)
    except ObjectDoesNotExist:
        page = None

    return render(request, 'pages/index.html', {'page': page})


def view_page(request, slug):
    try:
        page = Page.objects.get(slug=slug)
    except ObjectDoesNotExist:
        page = None

    return render(request, 'pages/index.html', {'page': page})


def delete_page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    page.delete()

    return redirect('home')


class PageUpdateView(UpdateView):
    model = Page
    fields = ('page_name', 'description', 'content', 'logo', 'is_mainpage')
    template_name = 'pages/NewEditPage.html'
    context_object_name = 'page'
    slug_field = 'slug'

    def form_valid(self, form):
        page = form.save(commit=False)
        page.updated_by = self.request.user
        page.updated_at = timezone.now()
        page.save()
        return redirect('pages.view.page', slug=page.slug)


@permission_required('pages.add_page')
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
    return render(request, 'pages/NewEditPage.html', {'form': form})
