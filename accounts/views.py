from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm
from .models import  Profile


def gravatar(user):
    email = user.email.lower().encode('utf-8')
    default = 'mm'
    size = 256
    url = 'https://www.gravatar.com/avatar/{md5}?{params}'.format(
        md5=hashlib.md5(email).hexdigest(),
        params=(urlencode({'d': default, 's': str(size)}))
    )
    return url


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'view_account.html'
    success_url = reverse_lazy('view_account')

    def get_location(self, instance):
        return instance.profile.location
    get_location.short_description = 'Location'

    def get_avatar(self, instance):
        if instance.profile.use_gravatar:
            return gravatar(user=instance.profile.user)

        return ''
    get_avatar.short_description = 'Current Avatar'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        user = form.save(commit=False)
        user.profile.save()
        user.save()

        return redirect('view_account')
